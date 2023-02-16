# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playgame_host.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        Main.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 73, 75, 255), stop:0.997452 rgba(255, 189, 96, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.credit = QtWidgets.QLabel(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(0, 560, 801, 31))
        self.credit.setStyleSheet("color:white;background-color:none;")
        self.credit.setAlignment(QtCore.Qt.AlignCenter)
        self.credit.setObjectName("credit")
        self.currentbalance = QtWidgets.QLabel(self.centralwidget)
        self.currentbalance.setGeometry(QtCore.QRect(510, 460, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.currentbalance.setFont(font)
        self.currentbalance.setStyleSheet("background:none;")
        self.currentbalance.setAlignment(QtCore.Qt.AlignCenter)
        self.currentbalance.setObjectName("currentbalance")
        self.startgame = QtWidgets.QPushButton(self.centralwidget)
        self.startgame.setGeometry(QtCore.QRect(50, 460, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startgame.setFont(font)
        self.startgame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startgame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.startgame.setObjectName("startgame")
        self.exit = QtWidgets.QLabel(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(730, 20, 55, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("QLabel {\n"
"background:none;\n"
"}\n"
"QLabel::hover {\n"
"background:none;\n"
"color:white;\n"
"}")
        self.exit.setAlignment(QtCore.Qt.AlignCenter)
        self.exit.setObjectName("exit")
        self.idroom = QtWidgets.QLabel(self.centralwidget)
        self.idroom.setGeometry(QtCore.QRect(590, 20, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idroom.setFont(font)
        self.idroom.setStyleSheet("background:none;")
        self.idroom.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.idroom.setObjectName("idroom")
        self.playercount = QtWidgets.QLabel(self.centralwidget)
        self.playercount.setGeometry(QtCore.QRect(10, 20, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.playercount.setFont(font)
        self.playercount.setStyleSheet("background:none;")
        self.playercount.setObjectName("playercount")
        self.roomname = QtWidgets.QLabel(self.centralwidget)
        self.roomname.setGeometry(QtCore.QRect(320, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.roomname.setFont(font)
        self.roomname.setStyleSheet("background:none;")
        self.roomname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.roomname.setObjectName("roomname")
        self.listplayer = QtWidgets.QListWidget(self.centralwidget)
        self.listplayer.setGeometry(QtCore.QRect(30, 150, 751, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listplayer.setFont(font)
        self.listplayer.setObjectName("listplayer")
        item = QtWidgets.QListWidgetItem()
        self.listplayer.addItem(item)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 90, 801, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background:none;")
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Game Bầu Cua Online - In Game"))
        self.credit.setText(_translate("Main", "Game made by MHP. You can buy me a cup of coffee through https://www.buymeacoffee.com/py.hacker.hieu, thank you very much."))
        self.currentbalance.setText(_translate("Main", "Tiền còn lại: 0 MHPoint"))
        self.startgame.setText(_translate("Main", "Bắt đầu"))
        self.exit.setText(_translate("Main", "X"))
        self.idroom.setText(_translate("Main", "ID:"))
        self.playercount.setText(_translate("Main", "Số người chơi: 0/0"))
        self.roomname.setText(_translate("Main", "Tên phòng:"))
        __sortingEnabled = self.listplayer.isSortingEnabled()
        self.listplayer.setSortingEnabled(False)
        self.listplayer.setSortingEnabled(__sortingEnabled)
        self.title.setText(_translate("Main", "Thống kê lựa chọn của người chơi"))