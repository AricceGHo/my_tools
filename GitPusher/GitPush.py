import sys
import subprocess as sub

from PyQt5 import QtWidgets
import git_push_ui


class ExampleApp(QtWidgets.QMainWindow, git_push_ui.Ui_Form):

    def open_rep_button_click(self):
        raise NotImplementedError
    def save_rep_list(self):
        raise NotImplementedError
    def load_rep_list(self):
        raise NotImplementedError
    def push_to_rep(self):
        raise NotImplementedError


    def __init__(self):

        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()ntcnefsesef


"""bash_command = 'sudo git push pytest master'
lst=bash_command.split()
password = '789123'
push = sub.Popen([lst[0],lst[1],lst[2],lst[3],lst[4]],
                 stdout=sub.PIPE, stderr=sub.PIPE)
stdout, stderr = push.communicate(input=password)
print(stdout)
print(stderr)"""