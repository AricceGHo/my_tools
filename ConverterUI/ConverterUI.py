# -*- coding:utf-8 -*-
import os
import sys
from PyQt5 import QtWidgets
import ConverterUbuntuUI
import json
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class ExampleApp(QtWidgets.QMainWindow, ConverterUbuntuUI.Ui_Form):
    def button_click_open(self):
        filters = "User Interface (*.ui)"
        f_dir = os.path.dirname(__file__)
        file_name_ui = QtWidgets.QFileDialog.getOpenFileName(
            None, "Выберете UI файл", f_dir, filters)
        self.file_name_ui = file_name_ui[0]

    def new_convert(self):
        filters = "Py файлы (*.py)"
        if self.f_dir == "":
            self.f_dir = os.path.dirname(__file__)

        file_name_py = QtWidgets.QFileDialog.getSaveFileName(
            None, "Назовите файл", self.f_dir, filters)
        self.file_name_py = file_name_py[0]
        self.file_name_f, file_extention = os.path.splitext(self.file_name_py)

        if file_extention == '.py':

            self.file_name_f = self.file_name_py

        else:
            self.file_name_f = self.file_name_py+".py"

    def button_click_convert(self):

        if self.comb == "New":
            self.new_convert()

        bash_command = "pyuic5 %s -o %s" % (
            self.file_name_ui, self.file_name_py)
        os.system(bash_command)
        print("vse ok")

    def button_click_save(self):
        try:

            filters = "JSON файлы (*.json)"
            f_dir = os.path.dirname(__file__)
            file_name = QtWidgets.QFileDialog.getSaveFileName(
                None, "Назовите файл настроек", f_dir, filters)
            file_name_f, file_extention = os.path.splitext(file_name[0])

            if file_extention == '.json':
                file_name_f = file_name[0]

            else:
                file_name_f = file_name[0]+".json"

            self.json_data_st = {"ui_data": self.json_data}
            with open(file_name_f, "w") as write_file:

                json.dump(self.json_data_st, write_file)

        except Exception as e:
            print(e)
            print('tuta')

    def button_click_load(self):
        try:
            self.comboBox.addItem("New")
            filters = "JSON файлы (*.json)"
            f_dir = os.path.dirname(__file__)
            file_name = QtWidgets.QFileDialog.getOpenFileName(
                None, "Выберете файл настроек", f_dir, filters)
            with open(file_name[0], 'r') as read_file:
                self.settings = json.load(read_file)

            for i in range(len(self.settings["ui_data"])):
                self.comboBox.addItem(self.settings["ui_data"][i]["name"])

            self.save_last_settings(file_name[0])

        except Exception as e:
            print(e)

    def same_folder_checkbox(self, state):
        if state == Qt.Checked:
            self.f_dir = os.path.dirname(self.file_name_ui)

    def onActivated(self, text):
        self.comb = text
        for i in range(len(self.settings["ui_data"])):
            if self.settings["ui_data"][i]["name"] == text:
                self.file_name_ui = self.settings["ui_data"][i]["ui_path"]
                self.file_name_py = self.settings["ui_data"][i]["py_path"]

    def button_click_remember(self):
        self.json_string = {"name": "%s" % self.name_lineEdit.text(), "ui_path": "%s" % (
            self.file_name_ui), "py_path": "%s" % (self.file_name_py)}
        self.json_data.append(self.json_string)

    def load_last_settings(self):
        try:
            self.settings_file = os.path.dirname(
                __file__)+"/last_settings.json"
            with open(self.settings_file, 'r') as read_file:
                self.last_settings = json.load(read_file)
            self.comboBox.addItem("New")
            with open(self.last_settings["last_settings_file_dir"], 'r') as read_file:
                self.settings = json.load(read_file)
            for i in range(len(self.settings["ui_data"])):
                self.comboBox.addItem(self.settings["ui_data"][i]["name"])
        except FileNotFoundError:
            pass

    def save_last_settings(self, settings_dir):
        self.last_settings = {"last_settings_file_dir": "%s" % (settings_dir)}
        with open(self.settings_file, "w") as write_file:
            json.dump(self.last_settings, write_file)

    def params_set(self):
        self.file_name_ui = ""
        self.file_name_py = ""
        self.json_string = ""
        self.json_data = []
        self.comb = "New"
        self.f_dir = ""

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.params_set()
        self.load_last_settings()
        self.comboBox.activated[str].connect(self.onActivated)
        self.openButton.clicked.connect(self.button_click_open)
        self.converButton.clicked.connect(self.button_click_convert)
        self.saveButton.clicked.connect(self.button_click_save)
        self.loadButton.clicked.connect(self.button_click_load)
        self.sameBox.stateChanged.connect(self.same_folder_checkbox)
        self.remButton.clicked.connect(self.button_click_remember)

    def initUI(self):
        f_dir = os.path.dirname(__file__)
        self.setWindowIcon(QIcon(f_dir+'/reload.svg'))
        self.saveButton.setIcon(QIcon(f_dir+'/save.png'))


def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp() 
    window.show()
    app.exec_() 


if __name__ == '__main__':
    main()
