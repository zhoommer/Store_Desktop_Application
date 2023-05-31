# from PyQt5.QtSql import QSqlDatabase
import sys
import mysql.connector as mc
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5 import Qt
import time



class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('ui_files/login.ui', self)
        self.btn_login.clicked.connect(self.login_page)

    def db_connection(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "E1ka3Hi49c&55^*a",
                database = "store_desk_app"
            )

            print("Connection Success")
        except mc.Error as e:
            print("Error in connection: " + e)
    def login_page(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "E1ka3Hi49c&55^*a",
                database = "store_desk_app"
            )

            # print("Connection Success")
        
            username = self.txt_username.text()
            password = self.txt_password.text()
            cursor = mydb.cursor()
            query = "SELECT * FROM users WHERE username='"+ username +"' and password='"+ password +"'"

            cursor.execute(query)

            res = cursor.fetchone()

            if res == None:
               self.lbl_error.setText("Kullanıcı adı ve ya parola yanlış!")

            else:
                mainForm = MainMenu()
                widget.addWidget(mainForm)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                widget.showFullScreen()
        except mc.Error as e:
            self.lbl_error.setText("Kullanıcı adı ve ya parola yanlış!")


class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi('ui_files/mainMenu.ui', self)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginForm = Login()
widget.addWidget(loginForm)
widget.setCurrentIndex(0)
# widget.setFixedWidth(800)
# widget.setFixedHeight(800)
widget.show()
app.exec_()

