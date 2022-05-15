# -*- coding: utf-8 -*-

"""
***************************************************************************
    DeletePreconfiguredAlgorithmAction.py
    ---------------------
    Date                 : April 2016
    Copyright            : (C) 2016 by Victor Olaya
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
__date__ = 'April 2016'
__copyright__ = '(C) 2016, Victor Olaya'

import os
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.core import QgsApplication
from processing.gui.ContextAction import ContextAction
from processing.preconfigured.PreconfiguredAlgorithm import PreconfiguredAlgorithm


class DeletePreconfiguredAlgorithmAction(ContextAction):

    def __init__(self):
        super().__init__()
        self.name = QCoreApplication.translate('DeletePreconfiguredAlgorithmAction', 'Delete Preconfigured Algorithm…')

    def isEnabled(self):
        return isinstance(self.itemData, PreconfiguredAlgorithm)

    def execute(self):
        reply = QMessageBox.question(None,
                                     self.tr('Delete Algorithm', 'DeletePreconfiguredAlgorithmAction'),
                                     self.tr('Are you sure you want to delete this algorithm?',
                                             'DeletePreconfiguredAlgorithmAction'),
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.remove(self.itemData.descriptionFile)
            QgsApplication.processingRegistry().providerById('preconfigured').refreshAlgorithms()
