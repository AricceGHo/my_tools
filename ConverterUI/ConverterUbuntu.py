import os
import sys
from PyQt5 import QtWidgets
import ConverterUbuntuUI


class ExampleApp(QtWidgets.QMainWindow, ConverterUbuntuUI.Ui_Form):

    def button_click_open(self):
        filters = "User Interface (*.ui)"
        f_dir = os.path.dirname(__file__)
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(
            None, "Выберете UI файл", f_dir, filters)
        

    def button_click_convert(self):
        filters = "Py файлы (*.py)"
        f_dir = os.path.dirname(__file__)
        file_name = QtWidgets.QFileDialog.getSaveFileName(
            None, "Назовите файл", f_dir, filters)
        print(file_name[0])
        file_name_f, file_extention= os.path.splitext(file_name[0])
        print(file_extention)
        if file_extention =='.py':
            file_name_f=file_name[0]
        
        else :
            file_name_f = file_name[0]+".py"
       

        #print(file_name_f)
        bash_command="pyuic5 %s -o %s" %(self.file_name[0],file_name_f)
        os.system(bash_command)

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.openButton.clicked.connect(self.button_click_open)
        self.converButton.clicked.connect(self.button_click_convert)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()ntcnefsesef
