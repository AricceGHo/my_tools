# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ariccegho/mytools/ConverterUI/ConverterUbuntu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(378, 119)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.openButton = QtWidgets.QPushButton(Form)
        self.openButton.setGeometry(QtCore.QRect(10, 10, 161, 25))
        self.openButton.setObjectName("openButton")
        self.converButton = QtWidgets.QPushButton(Form)
        self.converButton.setGeometry(QtCore.QRect(10, 50, 161, 25))
        self.converButton.setObjectName("converButton")
        self.sameBox = QtWidgets.QCheckBox(Form)
        self.sameBox.setGeometry(QtCore.QRect(190, 50, 111, 23))
        self.sameBox.setObjectName("sameBox")
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(180, 10, 51, 25))
        self.loadButton.setObjectName("loadButton")
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(350, 10, 21, 25))
        self.saveButton.setAcceptDrops(False)
        self.saveButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setObjectName("saveButton")
        self.name_lineEdit = QtWidgets.QLineEdit(Form)
        self.name_lineEdit.setGeometry(QtCore.QRect(240, 10, 113, 25))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 161, 25))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ConverterPYQT"))
        self.openButton.setText(_translate("Form", "Открыть файл .ui"))
        self.converButton.setText(_translate("Form", "Конвертировать в .py"))
        self.sameBox.setText(_translate("Form", "Та же папка"))
        self.loadButton.setText(_translate("Form", " Load"))
        self.name_lineEdit.setText(_translate("Form", "Название"))
