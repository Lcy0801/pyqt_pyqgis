# -*- coding: utf-8 -*-

"""
***************************************************************************
    AlgorithmDialog.py
    ---------------------
    Date                 : August 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'August 2012'
__copyright__ = '(C) 2012, Victor Olaya'

from pprint import pformat
import time

from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QMessageBox, QPushButton, QDialogButtonBox
from qgis.PyQt.QtGui import QColor, QPalette

from qgis.core import (Qgis,
                       QgsApplication,
                       QgsProcessingAlgRunnerTask,
                       QgsProcessingOutputHtml,
                       QgsProcessingAlgorithm,
                       QgsProxyProgressTask,
                       QgsProcessingFeatureSourceDefinition)
from qgis.gui import (QgsGui,
                      QgsProcessingAlgorithmDialogBase)
from qgis.utils import iface

from processing.core.ProcessingLog import ProcessingLog
from processing.core.ProcessingConfig import ProcessingConfig
from processing.core.ProcessingResults import resultsList
from processing.gui.ParametersPanel import ParametersPanel
from processing.gui.BatchAlgorithmDialog import BatchAlgorithmDialog
from processing.gui.AlgorithmDialogBase import AlgorithmDialogBase
from processing.gui.AlgorithmExecutor import executeIterating, execute, execute_in_place
from processing.gui.Postprocessing import handleAlgorithmResults

from processing.tools import dataobjects


class AlgorithmDialog(QgsProcessingAlgorithmDialogBase):

    def __init__(self, alg, in_place=False, parent=None):
        super().__init__(parent)

        self.feedback_dialog = None
        self.in_place = in_place
        self.active_layer = iface.activeLayer() if self.in_place else None

        self.context = None
        self.feedback = None

        self.setAlgorithm(alg)
        self.setMainWidget(self.getParametersPanel(alg, self))

        if not self.in_place:
            self.runAsBatchButton = QPushButton(QCoreApplication.translate("AlgorithmDialog", "Run as Batch Process…"))
            self.runAsBatchButton.clicked.connect(self.runAsBatch)
            self.buttonBox().addButton(self.runAsBatchButton,
                                       QDialogButtonBox.ResetRole)  # reset role to ensure left alignment
        else:
            in_place_input_parameter_name = 'INPUT'
            if hasattr(alg, 'inputParameterName'):
                in_place_input_parameter_name = alg.inputParameterName()

            self.mainWidget().setParameters({in_place_input_parameter_name: self.active_layer})

            self.runAsBatchButton = None
            has_selection = self.active_layer and (self.active_layer.selectedFeatureCount() > 0)
            self.buttonBox().button(QDialogButtonBox.Ok).setText(
                QCoreApplication.translate("AlgorithmDialog", "Modify Selected Features")
                if has_selection else QCoreApplication.translate("AlgorithmDialog", "Modify All Features"))
            self.setWindowTitle(self.windowTitle() + ' | ' + self.active_layer.name())

        self.updateRunButtonVisibility()

    def getParametersPanel(self, alg, parent):
        panel = ParametersPanel(parent, alg, self.in_place, self.active_layer)
        return panel

    def runAsBatch(self):
        self.close()
        dlg = BatchAlgorithmDialog(self.algorithm().create(), parent=iface.mainWindow())
        dlg.show()
        dlg.exec_()

    def resetAdditionalGui(self):
        if not self.in_place:
            self.runAsBatchButton.setEnabled(True)

    def blockAdditionalControlsWhileRunning(self):
        if not self.in_place:
            self.runAsBatchButton.setEnabled(False)

    def setParameters(self, parameters):
        self.mainWidget().setParameters(parameters)

    def createProcessingParameters(self):
        if self.mainWidget() is None:
            return {}
        else:
            return self.mainWidget().createProcessingParameters()

    def runAlgorithm(self):
        self.feedback = self.createFeedback()
        self.context = dataobjects.createContext(self.feedback)

        checkCRS = ProcessingConfig.getSetting(ProcessingConfig.WARN_UNMATCHING_CRS)
        try:
            parameters = self.createProcessingParameters()

            if checkCRS and not self.algorithm().validateInputCrs(parameters, self.context):
                reply = QMessageBox.question(self, self.tr("Unmatching CRS's"),
                                             self.tr('Parameters do not all use the same CRS. This can '
                                                     'cause unexpected results.\nDo you want to '
                                                     'continue?'),
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.No:
                    return
            ok, msg = self.algorithm().checkParameterValues(parameters, self.context)
            if not ok:
                QMessageBox.warning(
                    self, self.tr('Unable to execute algorithm'), msg)
                return

            self.blockControlsWhileRunning()
            self.setExecutedAnyResult(True)
            self.cancelButton().setEnabled(False)

            self.iterateParam = None

            for param in self.algorithm().parameterDefinitions():
                if isinstance(parameters.get(param.name(), None), QgsProcessingFeatureSourceDefinition) and parameters[
                        param.name()].flags & QgsProcessingFeatureSourceDefinition.FlagCreateIndividualOutputPerInputFeature:
                    self.iterateParam = param.name()
                    break

            self.clearProgress()
            self.feedback.pushVersionInfo(self.algorithm().provider())
            if self.algorithm().provider().warningMessage():
                self.feedback.reportError(self.algorithm().provider().warningMessage())

            self.setProgressText(QCoreApplication.translate('AlgorithmDialog', 'Processing algorithm…'))

            self.setInfo(
                QCoreApplication.translate('AlgorithmDialog', '<b>Algorithm \'{0}\' starting&hellip;</b>').format(
                    self.algorithm().displayName()), escapeHtml=False)

            self.feedback.pushInfo(self.tr('Input parameters:'))
            display_params = []
            for k, v in parameters.items():
                display_params.append(
                    "'" + k + "' : " + self.algorithm().parameterDefinition(k).valueAsPythonString(v, self.context))
            self.feedback.pushCommandInfo('{ ' + ', '.join(display_params) + ' }')
            self.feedback.pushInfo('')
            start_time = time.time()

            if self.iterateParam:
                # Make sure the Log tab is visible before executing the algorithm
                try:
                    self.showLog()
                    self.repaint()
                except:
                    pass

                self.cancelButton().setEnabled(self.algorithm().flags() & QgsProcessingAlgorithm.FlagCanCancel)
                if executeIterating(self.algorithm(), parameters, self.iterateParam, self.context, self.feedback):
                    self.feedback.pushInfo(
                        self.tr('Execution completed in {0:0.2f} seconds').format(time.time() - start_time))
                    self.cancelButton().setEnabled(False)
                    self.finish(True, parameters, self.context, self.feedback)
                else:
                    self.cancelButton().setEnabled(False)
                    self.resetGui()
            else:
                command = self.algorithm().asPythonCommand(parameters, self.context)
                if command:
                    ProcessingLog.addToLog(command)
                QgsGui.instance().processingRecentAlgorithmLog().push(self.algorithm().id())
                self.cancelButton().setEnabled(self.algorithm().flags() & QgsProcessingAlgorithm.FlagCanCancel)

                def on_complete(ok, results):
                    if ok:
                        self.feedback.pushInfo(
                            self.tr('Execution completed in {0:0.2f} seconds').format(time.time() - start_time))
                        self.feedback.pushInfo(self.tr('Results:'))
                        r = {k: v for k, v in results.items() if k not in ('CHILD_RESULTS', 'CHILD_INPUTS')}
                        self.feedback.pushCommandInfo(pformat(r))
                    else:
                        self.feedback.reportError(
                            self.tr('Execution failed after {0:0.2f} seconds').format(time.time() - start_time))
                    self.feedback.pushInfo('')

                    if self.feedback_dialog is not None:
                        self.feedback_dialog.close()
                        self.feedback_dialog.deleteLater()
                        self.feedback_dialog = None

                    self.cancelButton().setEnabled(False)

                    self.finish(ok, results, self.context, self.feedback, in_place=self.in_place)

                    self.feedback = None
                    self.context = None

                if not self.in_place and not (self.algorithm().flags() & QgsProcessingAlgorithm.FlagNoThreading):
                    # Make sure the Log tab is visible before executing the algorithm
                    self.showLog()

                    task = QgsProcessingAlgRunnerTask(self.algorithm(), parameters, self.context, self.feedback)
                    if task.isCanceled():
                        on_complete(False, {})
                    else:
                        task.executed.connect(on_complete)
                        self.setCurrentTask(task)
                else:
                    self.proxy_progress = QgsProxyProgressTask(
                        QCoreApplication.translate("AlgorithmDialog", "Executing “{}”").format(
                            self.algorithm().displayName()))
                    QgsApplication.taskManager().addTask(self.proxy_progress)
                    self.feedback.progressChanged.connect(self.proxy_progress.setProxyProgress)
                    self.feedback_dialog = self.createProgressDialog()
                    self.feedback_dialog.show()
                    if self.in_place:
                        ok, results = execute_in_place(self.algorithm(), parameters, self.context, self.feedback)
                    else:
                        ok, results = execute(self.algorithm(), parameters, self.context, self.feedback)
                    self.feedback.progressChanged.disconnect()
                    self.proxy_progress.finalize(ok)
                    on_complete(ok, results)

        except AlgorithmDialogBase.InvalidParameterValue as e:
            try:
                self.buttonBox().accepted.connect(lambda e=e:
                                                  e.widget.setPalette(QPalette()))
                palette = e.widget.palette()
                palette.setColor(QPalette.Base, QColor(255, 255, 0))
                e.widget.setPalette(palette)
            except:
                pass
            self.messageBar().clearWidgets()
            self.messageBar().pushMessage("", self.tr("Wrong or missing parameter value: {0}").format(
                e.parameter.description()),
                level=Qgis.Warning, duration=5)
        except AlgorithmDialogBase.InvalidOutputExtension as e:
            try:
                self.buttonBox().accepted.connect(lambda e=e:
                                                  e.widget.setPalette(QPalette()))
                palette = e.widget.palette()
                palette.setColor(QPalette.Base, QColor(255, 255, 0))
                e.widget.setPalette(palette)
            except:
                pass
            self.messageBar().clearWidgets()
            self.messageBar().pushMessage("", e.message,
                                          level=Qgis.Warning, duration=5)

    def finish(self, successful, result, context, feedback, in_place=False):
        keepOpen = not successful or ProcessingConfig.getSetting(ProcessingConfig.KEEP_DIALOG_OPEN)

        if not in_place and self.iterateParam is None:

            # add html results to results dock
            for out in self.algorithm().outputDefinitions():
                if isinstance(out, QgsProcessingOutputHtml) and out.name() in result and result[out.name()]:
                    resultsList.addResult(icon=self.algorithm().icon(), name=out.description(),
                                          timestamp=time.localtime(),
                                          result=result[out.name()])
            if not handleAlgorithmResults(self.algorithm(), context, feedback, not keepOpen, result):
                self.resetGui()
                return

        self.setExecuted(True)
        self.setResults(result)
        self.setInfo(self.tr('Algorithm \'{0}\' finished').format(self.algorithm().displayName()), escapeHtml=False)
        self.algorithmFinished.emit(successful, result)

        if not in_place and not keepOpen:
            self.close()
        else:
            self.resetGui()
            if self.algorithm().hasHtmlOutputs():
                self.setInfo(
                    self.tr('HTML output has been generated by this algorithm.'
                            '\nOpen the results dialog to check it.'), escapeHtml=False)
