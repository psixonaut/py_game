import sys
import datetime
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QListWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 867)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 415))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Error_out = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Error_out.setText("")
        self.Error_out.setObjectName("Error_out")
        self.verticalLayout.addWidget(self.Error_out)
        self.nodattim = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.nodattim.setObjectName("nodattim")
        self.verticalLayout.addWidget(self.nodattim)
        self.data_event = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.data_event.setObjectName("data_event")
        self.verticalLayout.addWidget(self.data_event)
        self.input_event = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_event.setObjectName("input_event")
        self.verticalLayout.addWidget(self.input_event)
        self.addtask = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addtask.setObjectName("addtask")
        self.verticalLayout.addWidget(self.addtask)
        self.openfile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openfile.setObjectName("openfile")
        self.verticalLayout.addWidget(self.openfile)
        self.updatelists = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.updatelists.setObjectName("updatelists")
        self.verticalLayout.addWidget(self.updatelists)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(410, 10, 371, 411))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.event_out_today = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.event_out_today.setObjectName("event_out_today")
        self.verticalLayout_2.addWidget(self.event_out_today)
        self.delete_event_today = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.delete_event_today.setObjectName("delete_event_today")
        self.verticalLayout_2.addWidget(self.delete_event_today)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 440, 371, 391))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.event_out_no_date = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.event_out_no_date.setObjectName("event_out_no_date")
        self.verticalLayout_3.addWidget(self.event_out_no_date)
        self.delete_event_btn_nodata = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.delete_event_btn_nodata.setObjectName("delete_event_btn_nodata")
        self.verticalLayout_3.addWidget(self.delete_event_btn_nodata)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(410, 440, 371, 391))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.event_out_yesterday = QtWidgets.QListWidget(self.verticalLayoutWidget_4)
        self.event_out_yesterday.setObjectName("event_out_yesterday")
        self.verticalLayout_4.addWidget(self.event_out_yesterday)
        self.delete_event_btn_yesterday = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.delete_event_btn_yesterday.setObjectName("delete_event_btn_yesterday")
        self.verticalLayout_4.addWidget(self.delete_event_btn_yesterday)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Планировщик"))
        self.nodattim.setText(_translate("MainWindow", "Без даты"))
        self.addtask.setText(_translate("MainWindow", "Добавить событее"))
        self.openfile.setText(_translate("MainWindow", "Открыть файл"))
        self.updatelists.setText(_translate("MainWindow", "Обновить"))
        self.label.setText(_translate("MainWindow", "Дела на сегодня"))
        self.delete_event_today.setText(_translate("MainWindow", "Удалить событее"))
        self.label_2.setText(_translate("MainWindow", "Дела без срока"))
        self.delete_event_btn_nodata.setText(_translate("MainWindow", "Удалить событее"))
        self.label_3.setText(_translate("MainWindow", "Просроченные дела"))
        self.delete_event_btn_yesterday.setText(_translate("MainWindow", "Удалить событее"))



class Window (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calendar.ui', self)

        self.con = sqlite3.connect('tasks_db.db')
        self.cur = self.con.cursor()
        self.addtask.clicked.connect(self.add_event_button)
        self.delete_event_today.clicked.connect(self.delete_event_today_button)
        self.delete_event_btn_yesterday.clicked.connect(self.delete_event_yesterday_button)
        self.delete_event_btn_nodata.clicked.connect(self.delete_event_no_date_button)
        self.updatelists.clicked.connect(self.button_refresh)
        self.openfile.clicked.connect(self.open_file_button)
        self.refresh_list()

    def add_event_button(self):     # кнопка добавить событее
        self.add_event()

    def add_event(self):     # добавление события
        current_event_name = self.input_event.text()
        t_event = None
        if current_event_name == '':
            self.Error_out.setText('Введите название события')
        else:
            self.Error_out.setText ('')
            if not self.nodattim.isChecked():
                t_event = datetime.date(self.data_event.selectedDate().year(),
                                        self.data_event.selectedDate().month(),
                                        self.data_event.selectedDate().day())
            self.insert_event(current_event_name, t_event)
            self.con.commit()
            self.input_event.clear()
            self.refresh_list()

    def insert_event(self, event_name, event_data):     # добавление в БД
        if event_data:
            self.cur.execute(f"INSERT INTO task (data, name) VALUES ('{event_data}', '{event_name}')")
        else:
            self.cur.execute(f"INSERT INTO task (name) VALUES ('{event_name}')")

    def select_events(self, flag_day):     # вызов из БД
        data_select = datetime.date.today()
        sql_select = f"SELECT * FROM task WHERE data = '{data_select}'"
        if flag_day == 1:
            sql_select = f"SELECT * FROM task WHERE data < '{data_select}'"
        elif flag_day == 2:
            sql_select = "SELECT * FROM task WHERE data is Null"
        today = self.cur.execute(sql_select).fetchall()
        return today

    def button_refresh(self):     # кнопка Обновить
        self.refresh_list()

    def refresh_list(self):     # обновление списков в дизайне
        today = self.select_events(flag_day=0)
        self.event_out_today.clear()
        self.list_fill(self.event_out_today, today)

        today = self.select_events(flag_day=1)
        self.event_out_yesterday.clear()
        self.list_fill(self.event_out_yesterday, today)

        today = self.select_events(flag_day=2)
        self.event_out_no_date.clear()
        self.list_fill(self.event_out_no_date, today)

    def list_fill(self, obj_list, list_found):     # заполнение списков
        for item in list_found:
            my_item = QListWidgetItem()
            my_item.setText(item[2])
            obj_list.addItem(my_item)
            my_item.setData(QtCore.Qt.UserRole, item[0])

    def open_file_button(self):     # кнопка открытия файлов
        self.open_file()

    def open_file(self):     # открытие и обработка файлов
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        with open(fname, encoding='utf8') as file:
            for line in file:
                temp = line.strip().split(';')
                if temp[0] == 0:
                    event_data = None
                else:
                    event_data = temp[0]
                    event_name = temp[1]
                self.insert_event(event_name, event_data)
            self.con.commit()
            self.refresh_list()

    def delete_event_today_button(self):     # кнопка удалить под списком сегодня
        self.delete_event_from_list(self.event_out_today)

    def delete_event_yesterday_button(self):     # кнопка удалить под списком просроченно
        self.delete_event_from_list(self.event_out_yesterday)

    def delete_event_no_date_button(self):     # кнопка удалить под списком без даты
        self.delete_event_from_list(self.event_out_no_date)

    def delete_event_from_list(self, list_name):    # определение выделенного элемента, который нужно удалить
        result = list_name.selectedItems()
        self.Error_out.setText('')
        if not result or len(result) <= 0:
            self.Error_out.setText('Выберите событее')
            return
        d = result[0].data(QtCore.Qt.UserRole)
        self.delete_event(d)

    def delete_event(self, event_id):     # удаление элемента из БД
        self.cur.execute(f"DELETE from task WHERE id = '{event_id}'")
        self.con.commit()
        self.refresh_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())

