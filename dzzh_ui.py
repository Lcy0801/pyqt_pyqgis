# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dzzh_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 500)
        Form.setMinimumSize(QtCore.QSize(900, 500))
        Form.setMaximumSize(QtCore.QSize(780, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/地质灾害.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.escButton = QtWidgets.QPushButton(Form)
        self.escButton.setObjectName("escButton")
        self.horizontalLayout.addWidget(self.escButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.zhTable = QtWidgets.QTableWidget(Form)
        self.zhTable.setObjectName("zhTable")
        self.zhTable.setColumnCount(0)
        self.zhTable.setRowCount(0)
        self.verticalLayout.addWidget(self.zhTable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "地质灾害查询"))
        self.label.setText(_translate("Form", "地震地质灾害结果表"))
        self.escButton.setText(_translate("Form", "返回"))
