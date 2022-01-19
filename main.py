import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox


def except_hook(cls, exception, traceback) -> None:
    sys.__excepthook__(cls, exception, traceback)

#приветственное меню
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

#меню с играми
class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('menu_2.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.to_tet_game)
        self.pushButton_2.clicked.connect(self.to_snake_game)
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.to_shooter_game)
        self.pushButton_5.clicked.connect(self.to_arcanoid_game)
        self.pushButton_6.clicked.connect(self.to_tictactoe_game)

    def back(self):
        back = Greet_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, back)
        widg.setCurrentIndex(index)

    def to_shooter_game(self):
        background = Background('shooter')
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background)
        widg.setCurrentIndex(index)

    def to_tictactoe_game(self):
        background = Background('tictactoe')
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background)
        widg.setCurrentIndex(index)

    def to_arcanoid_game(self):
        background = Background('arcanoid')
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background)
        widg.setCurrentIndex(index)

    def to_tet_game(self):
        background = Background('tetris')
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background)
        widg.setCurrentIndex(index)

    def to_snake_game(self):
        background = Background('snake')
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background)
        widg.setCurrentIndex(index)


into_profile = False

#страница с профилем/переход в регистрацию и вход
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
        global name_for_profile
        self.listWidget.addItem(name_for_profile)
        bd = sqlite3.connect("our_users_1.sqlite")
        cur = bd.cursor()
        tet_res, snake_res = cur.execute(f"""SELECT tetris_score, snake_score FROM users_info
                                             WHERE name = '{name_for_profile}'""").fetchone()
        self.listWidget_2.addItem(str(tet_res))
        self.listWidget_3.addItem(str(snake_res))
        self.pushButton_4.clicked.connect(self.to_logout)
        self.show()

    def initUI0(self):
        loadUi('profile_without_info.ui', self)
        self.pushButton.clicked.connect(self.to_login)
        self.pushButton_2.clicked.connect(self.to_signup)
        self.pushButton_3.clicked.connect(self.to_back)
        self.show()

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

    def to_logout(self):
        global into_profile
        into_profile = False
        login = Login_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, login)
        widg.setCurrentIndex(index)

    def to_back(self):
        back = Greet_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, back)
        widg.setCurrentIndex(index)

#фон к играм
class Background(QDialog):
    def __init__(self, game):
        super(Background, self).__init__()
        self.initUI()
        self.game = game

    def initUI(self):
        loadUi('game_background.ui', self)
        self.pushButton.clicked.connect(self.init_pygame)
        self.pushButton_3.clicked.connect(self.to_menu)
        self.show()

    def init_pygame(self):
        if self.game == 'tetris':
            import tetris
        elif self.game == 'snake':
            import snake
        elif self.game == 'shooter':
            import space_invaders
        elif self.game == 'arcanoid':
            import arcanoid
        elif self.game == 'tictactoe':
            import tic_tac_toe

    def to_menu(self):
        menu = Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, menu)
        widg.setCurrentIndex(index)

name_for_profile = ''

#страница входа
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
        bd = sqlite3.connect("our_users_1.sqlite")
        cur = bd.cursor()
        all_login = cur.execute("""SELECT * FROM users_info""").fetchall()
        all_passwords = []
        all_names = []
        for i in all_login:
            all_names.append(i[0])
        for j in all_login:
            all_passwords.append(j[1])
        if name_info in all_names and passw_info in all_passwords:
            global name_for_profile
            global into_profile
            into_profile = True
            name_for_profile = name_info
            profile = Profile_Window()
            index = widg.currentIndex() + 1
            widg.insertWidget(index, profile)
            widg.setCurrentIndex(index)
        else:
            No_user()

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

#страница регистрации
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

        bd = sqlite3.connect("our_users_1.sqlite")
        cur = bd.cursor()
        all_login = cur.execute("""SELECT * FROM users_info""").fetchall()
        all_passwords = []
        all_names = []
        for i in all_login:
            all_names.append(i[0])
        for j in all_login:
            all_passwords.append(j[1])
        if name_info == '':
            Fail_name()
        if len(passw_info) >= 6 and not passw_info.isdigit() and not passw_info.isalpha():
            if name_info not in all_names:
                bd = sqlite3.connect("our_users_1.sqlite")
                cur = bd.cursor()
                cur.execute('INSERT INTO users_info VALUES (?, ?, 0, 0)', (name_info, passw_info))
                bd.commit()
                cur.close()
                bd.close()
                Success()
                self.to_login()
            else:
                InDB()
        else:
            Fail()

    def to_login(self):
        login = Login_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, login)
        widg.setCurrentIndex(index)

#уведомления
class InDB(QMessageBox):
    def __init__(self):
        super().__init__()
        mesage_maker = QMessageBox()
        mesage_maker.setWindowTitle('Pyminigames')
        mesage_maker.setText("Такой пользователь уже существует")
        mesage_maker.setIcon(QMessageBox.Critical)
        mesage_maker.setStandardButtons(QMessageBox.Ok)
        mesage_maker.setStyleSheet("color:rgb(47, 102, 144);\n"
                                   "background-color:rgb(129, 195, 215);\n"
                                   "border-radius: 30px;")
        start = mesage_maker.exec_()


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

class No_user(QMessageBox):
    def __init__(self):
        super().__init__()
        mesage_maker = QMessageBox()
        mesage_maker.setWindowTitle('Pyminigames')
        mesage_maker.setText("Неправильный пароль или имя пользователя")
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
