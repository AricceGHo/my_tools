# -*- coding:utf-8 -*-
import os
import sys
from PyQt5 import QtWidgets
import ConverterUbuntuUI
import json
from PyQt5.QtGui import QIcon

class ExampleApp(QtWidgets.QMainWindow, ConverterUbuntuUI.Ui_Form):

    def button_click_open(self):
        filters = "User Interface (*.ui)"
        f_dir = os.path.dirname(__file__)
        self.file_name_ui = QtWidgets.QFileDialog.getOpenFileName(
            None, "Выберете UI файл", f_dir, filters)
        

    def button_click_convert(self):
        filters = "Py файлы (*.py)"
        f_dir = os.path.dirname(__file__)
        self.file_name_py = QtWidgets.QFileDialog.getSaveFileName(
            None, "Назовите файл", f_dir, filters)
        
        file_name_f, file_extention= os.path.splitext(self.file_name_py[0])
       
        if file_extention =='.py':
            self.file_name_f=self.file_name_py[0]
        
        else :
            self.file_name_f = self.file_name_py[0]+".py"
       

        
        bash_command="pyuic5 %s -o %s" %(self.file_name_ui[0],self.file_name_f)
        os.system(bash_command)
    def button_click_save(self):
        try:
            json_string = {"%s"%(self.name_lineEdit.text()):{"ui_path": "%s" % (self.file_name_ui[0]), "py_path": "%s" % (self.file_name_py[0])}}
            filters = "JSON файлы (*.json)"
            f_dir = os.path.dirname(__file__)
            file_name = QtWidgets.QFileDialog.getSaveFileName(
                None, "Назовите файл настроек", f_dir, filters)
            file_name_f, file_extention = os.path.splitext(file_name[0])
            json_string_n=[[]]
            if file_extention == '.json':
                file_name_f = file_name[0]

            else:
                file_name_f = file_name[0]+".json"
            json_string_n.append(json_string)
            print(json_string_n)
            with open(file_name_f, "w") as write_file:
                
                json.dump(json_string_n, write_file)

        except Exception as e:
            print(e)
            print('tuta')

    def button_click_load(self):
        
        try:
            filters = "JSON файлы (*.json)"
            f_dir = os.path.dirname(__file__)
            file_name = QtWidgets.QFileDialog.getOpenFileName(
                None, "Выберете файл настроек", f_dir, filters)
            with open(file_name[0], 'r') as read_file:
                self.settings = json.load(read_file)
            self.file_name_ui=self.settings["ui_path"]
            self.file_name_py=self.settings["py_path"]
            print('ok')
            
        except(TypeError, FileNotFoundError):
            self.comboBox.addItem('Отмена загрузки файла настроек')
        except Exception as e:
            print(e)

    def same_folder_checkbox(self):
        print()
    

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.openButton.clicked.connect(self.button_click_open)
        self.converButton.clicked.connect(self.button_click_convert)
        self.saveButton.clicked.connect(self.button_click_save)
        self.loadButton.clicked.connect(self.button_click_load)
        self.sameBox.stateChanged.connect(self.same_folder_checkbox)

    def initUI(self):
        f_dir = os.path.dirname(__file__)
        self.setWindowIcon(QIcon(f_dir+'/reload.svg'))
        self.saveButton.setIcon(QIcon(f_dir+'/save.png'))
        


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()ntcnefsesef
