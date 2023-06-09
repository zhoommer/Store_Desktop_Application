# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 1200))
        MainWindow.setStyleSheet("background-color: #154360;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setMaximumSize(QtCore.QSize(600, 400))
        self.main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.main)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txt_username = QtWidgets.QLineEdit(self.main)
        self.txt_username.setMinimumSize(QtCore.QSize(0, 40))
        self.txt_username.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.txt_username.setFont(font)
        self.txt_username.setStyleSheet("color: #fff;")
        self.txt_username.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_username.setObjectName("txt_username")
        self.gridLayout_3.addWidget(self.txt_username, 0, 0, 1, 1)
        self.txt_password = QtWidgets.QLineEdit(self.main)
        self.txt_password.setMinimumSize(QtCore.QSize(0, 40))
        self.txt_password.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("color: #fff;")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout_3.addWidget(self.txt_password, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.main, 2, 0, 1, 1)
        self.footer = QtWidgets.QFrame(self.centralwidget)
        self.footer.setMaximumSize(QtCore.QSize(600, 400))
        self.footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.footer)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_login = QtWidgets.QPushButton(self.footer)
        self.btn_login.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_login.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("")
        self.btn_login.setObjectName("btn_login")
        self.gridLayout_4.addWidget(self.btn_login, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.footer, 3, 0, 1, 1, QtCore.Qt.AlignTop)
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(600, 400))
        self.header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.header)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.header)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.header, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txt_username.setPlaceholderText(_translate("MainWindow", "Kullanici Adi"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "Sifre"))
        self.btn_login.setText(_translate("MainWindow", "Giris Yap"))
        self.label.setText(_translate("MainWindow", "Giris Yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
