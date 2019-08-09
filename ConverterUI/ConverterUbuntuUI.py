# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ariccegho/git/PythonProjects/ConverterUI/ConverterUbuntu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(183, 91)
        self.openButton = QtWidgets.QPushButton(Form)
        self.openButton.setGeometry(QtCore.QRect(10, 10, 161, 25))
        self.openButton.setObjectName("openButton")
        self.converButton = QtWidgets.QPushButton(Form)
        self.converButton.setGeometry(QtCore.QRect(10, 50, 161, 25))
        self.converButton.setObjectName("converButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ConverterPYQT"))
        self.openButton.setText(_translate("Form", "Открыть файл .ui"))
        self.converButton.setText(_translate("Form", "Конвертировать в .py"))
