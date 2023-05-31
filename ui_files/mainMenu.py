# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../5440b1d2/9071175_all_application_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setStyleSheet("QLabel {\n"
"    color: #fff;\n"
"}\n"
"\n"
"background-color: #29406C;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.main_menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_menu_frame.setStyleSheet("background-color: #29406C;")
        self.main_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_menu_frame.setObjectName("main_menu_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_menu_frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.main_menu_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 75, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_new_sales = QtWidgets.QPushButton(self.frame_6)
        self.btn_new_sales.setMinimumSize(QtCore.QSize(150, 150))
        self.btn_new_sales.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.btn_new_sales.setFont(font)
        self.btn_new_sales.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_new_sales.setStyleSheet("background-color: orange; border: none; color: #fff;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/4534d81e/cart-shopping-fast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new_sales.setIcon(icon1)
        self.btn_new_sales.setObjectName("btn_new_sales")
        self.gridLayout_4.addWidget(self.btn_new_sales, 0, 0, 1, 1)
        self.btn_reprint = QtWidgets.QPushButton(self.frame_6)
        self.btn_reprint.setMinimumSize(QtCore.QSize(150, 150))
        self.btn_reprint.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.btn_reprint.setFont(font)
        self.btn_reprint.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reprint.setStyleSheet("border: none; background-color: #82F106; color: #fff;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/1f4b6858/print-magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reprint.setIcon(icon2)
        self.btn_reprint.setObjectName("btn_reprint")
        self.gridLayout_4.addWidget(self.btn_reprint, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.main_menu_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout_5.addWidget(self.frame_7, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_6.setContentsMargins(0, 74, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_7.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border: none; background-color: #82F106; color: #fff; margin-top: 3px;")
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_6.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_6.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border: none; background-color: #027FDB; color: #fff; margin-top: 3px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_6.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border: none; background-color: orange; color: #fff;")
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border: none; background-color: #027FDB; color: #fff; margin-top: 3px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border: none; background-color: #027FDB; color: #fff; margin-top: 3px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border: none; background-color: #027FDB; color: #fff; margin-top: 3px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border: none; background-color: #027FDB; color: #fff;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_8, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.main_menu_frame)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.gridLayout_7.addWidget(self.frame_9, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_8.setContentsMargins(0, 75, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_8.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_8.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("border: none; background-color: orange; color: #fff;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/ec9eb456/sack-dollar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_8.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_9.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_9.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("border: none; background-color: #82F106; color: #fff;")
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_8.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_10, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 2, 1, 1, QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.main_menu_frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gridLayout_9.addWidget(self.frame_11, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_10.setContentsMargins(0, 75, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_10.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_10.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("border: none; background-color: #027FDB; color: #fff;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_10.addWidget(self.pushButton_10, 0, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_11.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_11.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("border: none; background-color: #027FDB; color: #fff;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_10.addWidget(self.pushButton_11, 0, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_12.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_12.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("border: none; background-color: #027FDB; color: #fff; margin-top: 3px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_10.addWidget(self.pushButton_12, 1, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_13.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButton_13.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("border: none; background-color: #027FDB; color: #fff; margin-top: 3px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_10.addWidget(self.pushButton_13, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.frame_12, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 0, 3, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(self.main_menu_frame, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("folder-open")
        self.actionOpen.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setBold(False)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.actionSave.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.actionSave_As.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionSave_As.setFont(font)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_All = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.actionSave_All.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionSave_All.setFont(font)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("system-shutdown")
        self.actionClose.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionClose.setFont(font)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.actionQuit.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionQuit.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-undo")
        self.actionUndo.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionUndo.setFont(font)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-redo")
        self.actionRedo.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionRedo.setFont(font)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-cut")
        self.actionCut.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionCut.setFont(font)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-copy")
        self.actionCopy.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionCopy.setFont(font)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPast = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.actionPast.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionPast.setFont(font)
        self.actionPast.setObjectName("actionPast")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("edit-select-all")
        self.actionSelect_All.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.actionSelect_All.setFont(font)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addAction(self.actionSave)
        self.menuNew.addAction(self.actionSave_As)
        self.menuNew.addAction(self.actionSave_All)
        self.menuNew.addAction(self.actionClose)
        self.menuNew.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPast)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IT STORE"))
        self.label.setText(_translate("MainWindow", "     Peşin Satış"))
        self.btn_new_sales.setText(_translate("MainWindow", " Yeni"))
        self.btn_reprint.setText(_translate("MainWindow", " Yeniden Yazdır"))
        self.label_2.setText(_translate("MainWindow", "     Peşin Satış İade"))
        self.pushButton_7.setText(_translate("MainWindow", " Yeniden Yazdır"))
        self.pushButton_6.setText(_translate("MainWindow", "Ürün İade Al"))
        self.pushButton.setText(_translate("MainWindow", " Yeni"))
        self.pushButton_5.setText(_translate("MainWindow", "Ürün Değiştir"))
        self.pushButton_4.setText(_translate("MainWindow", "Ürün Varyant \n"
"Değiştir"))
        self.pushButton_3.setText(_translate("MainWindow", "Ürün İade Al \n"
"(E-Fatura)"))
        self.pushButton_2.setText(_translate("MainWindow", "Tümünü İade \n"
"Al"))
        self.label_3.setText(_translate("MainWindow", "     Masraflar"))
        self.pushButton_8.setText(_translate("MainWindow", " Masraf Faturası"))
        self.pushButton_9.setText(_translate("MainWindow", " Yeniden Yazdır"))
        self.label_4.setText(_translate("MainWindow", "     Raporlar"))
        self.pushButton_10.setText(_translate("MainWindow", "Perakende\n"
"Müşteri\n"
"Ekstresi"))
        self.pushButton_11.setText(_translate("MainWindow", "Alınan\n"
"Ödemeler\n"
"Listesi"))
        self.pushButton_12.setText(_translate("MainWindow", "Perakende\n"
"Satışlar Listesi"))
        self.pushButton_13.setText(_translate("MainWindow", "Mağaza\n"
"Hareket Özeti"))
        self.menuNew.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUndo.setText(_translate("MainWindow", "Undo Ctrl+Z"))
        self.actionUndo.setToolTip(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPast.setText(_translate("MainWindow", "Paste"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
