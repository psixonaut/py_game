import random
import sys
import pygame
import sqlite3
import os
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import pygame
from PyQt5.uic import loadUi
from copy import deepcopy
from random import choice
from PyQt5.QtWidgets import QMessageBox
from pygame import mixer

def except_hook(cls, exception, traceback) -> None:
    sys.__excepthook__(cls, exception, traceback)


class Greet_Window(QDialog):
    def __init__(self):
        super(Greet_Window, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('main_menu.ui', self)
        self.pushButton.clicked.connect(self.to_menu)
        self.pushButton_2.clicked.connect(self.to_profile)
        self.show()

    def to_menu(self):
        menu = Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, menu)
        widg.setCurrentIndex(index)

    def to_profile(self):
        profile = Profile_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, profile)
        widg.setCurrentIndex(index)


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

        # mixer.music.load('music.wav.mp3')
        # mixer.music.play(-1)
    def initUI(self):
        loadUi('menu_2.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.to_tet_game)
        self.pushButton_2.clicked.connect(self.to_snake_game)
        self.pushButton_3.clicked.connect(self.back)

    def back(self):
        back = Greet_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, back)
        widg.setCurrentIndex(index)

    def to_tet_game(self):
        background = Background()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background)
        widg.setCurrentIndex(index)

    def to_snake_game(self):
        background1 = Background1()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background1)
        widg.setCurrentIndex(index)


into_profile = False


class Profile_Window(QDialog):
    def __init__(self):
        super(Profile_Window, self).__init__()
        if into_profile is True:
            self.initUI()
        else:
            self.initUI0()

    def initUI(self):
        loadUi('profile.ui', self)
        self.pushButton_3.clicked.connect(self.to_back)
        self.show()

    def initUI0(self):
        loadUi('profile_without_info.ui', self)
        self.pushButton.clicked.connect(self.to_login)
        self.pushButton_2.clicked.connect(self.to_signup)
        self.pushButton_3.clicked.connect(self.to_back)
        self.show()
        self.fill_info()

    def fill_info(self):
        pass

    def to_signup(self):
        signup = Signup_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, signup)
        widg.setCurrentIndex(index)

    def to_login(self):
        login = Login_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, login)
        widg.setCurrentIndex(index)

    def to_back(self):
        back = Greet_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, back)
        widg.setCurrentIndex(index)


class Background(QDialog):
    def __init__(self):
        super(Background, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('game_background.ui', self)
        self.pushButton.clicked.connect(self.init_pygame)
        self.pushButton_2.clicked.connect(self.to_stop)
        self.pushButton_3.clicked.connect(self.to_menu)
        self.show()

    def init_pygame(self):
        import tetris

    def to_menu(self):
        menu = Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, menu)
        widg.setCurrentIndex(index)

    def to_stop(self):
        pass


class Background1(QDialog):
    def __init__(self):
        super(Background1, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('game_background.ui', self)
        self.pushButton.clicked.connect(self.init_pygame)
        self.pushButton_2.clicked.connect(self.to_stop)
        self.pushButton_3.clicked.connect(self.to_menu)
        self.show()

    def init_pygame(self):
        import snake

    def to_menu(self):
        menu = Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, menu)
        widg.setCurrentIndex(index)

    def to_stop(self):
        pass


class Login_Window(QDialog):
    def __init__(self):
        super(Login_Window, self).__init__()
        loadUi("login.ui", self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.to_signup)
        self.show()


    def login(self):
        name_info = self.lineEdit.text()
        passw_info = self.lineEdit_2.text()
        bd = sqlite3.connect("our_users.sqlite")
        cur = bd.cursor()
        all_names = cur.execute("""SELECT * FROM name""").fetchall()
        #print('i')
        all_passwords = cur.execute("""SELECT * FROM password""").fetchall()
        #print(all_names, all_passwords)
        self.bd.commit()
        self.bd.close()
        if name_info in all_names and passw_info in all_passwords:
            into_profile = True
            # global name_info
            # global passw_info
            profile = Profile_Window()
            index = widg.currentIndex() + 1
            widg.insertWidget(index, profile)
            widg.setCurrentIndex(index)

    def to_back(self):
        back = Greet_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, back)
        widg.setCurrentIndex(index)

    def to_signup(self):
        signup = Signup_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, signup)
        widg.setCurrentIndex(index)


class Signup_Window(QDialog):
    def __init__(self):
        super(Signup_Window, self).__init__()
        loadUi("signin.ui", self)
        self.pushButton.clicked.connect(self.signup)
        self.pushButton_2.clicked.connect(self.to_login)
        self.show()

    def to_back(self):
        back = Greet_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, back)
        widg.setCurrentIndex(index)

    def signup(self):
        name_info = self.lineEdit.text()
        passw_info = self.lineEdit_2.text()
        if name_info == '':
            Fail_name()
        if len(passw_info) >= 6 and not passw_info.isdigit() and not passw_info.isalpha():
            bd = sqlite3.connect("users_information.sqlite")
            cur = bd.cursor()
            cur.execute('INSERT INTO users VALUES (?)', (name_info))
            bd.commit()
            cur.close()
            bd.close()
            Success()
            self.to_login()
        else:
            Fail()

    def to_login(self):
        login = Login_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, login)
        widg.setCurrentIndex(index)


class Fail(QMessageBox):
    def __init__(self):
        super().__init__()
        mesage_maker = QMessageBox()
        mesage_maker.setWindowTitle('Pyminigames')
        mesage_maker.setText("Должно быть не меньше 6 символов, а пароль состоять из букв и цифр")
        mesage_maker.setIcon(QMessageBox.Critical)
        mesage_maker.setStandardButtons(QMessageBox.Ok)
        mesage_maker.setStyleSheet("color:rgb(47, 102, 144);\n"
                                   "background-color:rgb(129, 195, 215);\n"
                                   "border-radius: 30px;")
        start = mesage_maker.exec_()


class Fail_name(QMessageBox):
    def __init__(self):
        super().__init__()
        mesage_maker = QMessageBox()
        mesage_maker.setWindowTitle('Pyminigames')
        mesage_maker.setText("Не введено имя")
        mesage_maker.setIcon(QMessageBox.Critical)
        mesage_maker.setStandardButtons(QMessageBox.Ok)
        mesage_maker.setStyleSheet("color:rgb(47, 102, 144);\n"
                                   "background-color:rgb(129, 195, 215);\n"
                                   "border-radius: 30px;")
        start = mesage_maker.exec_()


class Success(QMessageBox):
    def __init__(self):
        super().__init__()
        mesage_maker = QMessageBox()
        mesage_maker.setWindowTitle('Pyminigames')
        mesage_maker.setText("Поздравляем с регистрацией!")
        mesage_maker.setIcon(QMessageBox.Information)
        mesage_maker.setStandardButtons(QMessageBox.Ok)
        mesage_maker.setStyleSheet("color:rgb(47, 102, 144);\n"
                                   "background-color:rgb(129, 195, 215);\n"
                                   "border-radius: 30px;")
        start = mesage_maker.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    grt_wnd = Greet_Window()
    wnd = Window()
    widg = QtWidgets.QStackedWidget()

    widg.addWidget(grt_wnd)
    widg.addWidget(wnd)

    widg.setFixedWidth(1920)
    widg.setFixedHeight(1000)
    widg.setWindowTitle('Pyminigames')
    widg.show()
    result = app.exec_()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
