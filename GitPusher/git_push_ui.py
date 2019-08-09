# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ariccegho/git/GitPusher/GitPusher.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 123)
        self.open_repButton = QtWidgets.QPushButton(Form)
        self.open_repButton.setGeometry(QtCore.QRect(0, 10, 171, 31))
        self.open_repButton.setObjectName("open_repButton")
        self.save_repButton = QtWidgets.QPushButton(Form)
        self.save_repButton.setGeometry(QtCore.QRect(180, 10, 89, 31))
        self.save_repButton.setObjectName("save_repButton")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 50, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pullButton = QtWidgets.QPushButton(Form)
        self.pullButton.setGeometry(QtCore.QRect(110, 50, 89, 25))
        self.pullButton.setObjectName("pullButton")
        self.fetchButton = QtWidgets.QPushButton(Form)
        self.fetchButton.setGeometry(QtCore.QRect(210, 50, 89, 25))
        self.fetchButton.setObjectName("fetchButton")
        self.passEdit = QtWidgets.QLineEdit(Form)
        self.passEdit.setGeometry(QtCore.QRect(120, 90, 113, 25))
        self.passEdit.setObjectName("passEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.label.setObjectName("label")
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(280, 10, 89, 31))
        self.loadButton.setObjectName("loadButton")
        self.mergeButton = QtWidgets.QPushButton(Form)
        self.mergeButton.setGeometry(QtCore.QRect(310, 50, 89, 25))
        self.mergeButton.setObjectName("mergeButton")
        self.rep_chooseBox = QtWidgets.QComboBox(Form)
        self.rep_chooseBox.setGeometry(QtCore.QRect(380, 10, 21, 31))
        self.rep_chooseBox.setObjectName("rep_chooseBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GitPusher"))
        self.open_repButton.setText(_translate("Form", "Открыть репозиторий"))
        self.save_repButton.setText(_translate("Form", "Сохранить"))
        self.pushButton.setText(_translate("Form", "Push"))
        self.pullButton.setText(_translate("Form", "Pull"))
        self.fetchButton.setText(_translate("Form", "Fetch"))
        self.label.setText(_translate("Form", "Пароль SUDO: "))
        self.loadButton.setText(_translate("Form", "Загрузить"))
        self.mergeButton.setText(_translate("Form", "Merge"))
