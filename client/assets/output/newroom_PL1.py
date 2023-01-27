# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newroom_PL1.ui'
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
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 150, 801, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background:none;")
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.credit = QtWidgets.QLabel(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(0, 560, 801, 31))
        self.credit.setStyleSheet("color:white;background-color:none;")
        self.credit.setAlignment(QtCore.Qt.AlignCenter)
        self.credit.setObjectName("credit")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(0, 220, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.description.setFont(font)
        self.description.setStyleSheet("background:none;")
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.host = QtWidgets.QPushButton(self.centralwidget)
        self.host.setGeometry(QtCore.QRect(120, 320, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.host.setFont(font)
        self.host.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.host.setObjectName("host")
        self.player = QtWidgets.QPushButton(self.centralwidget)
        self.player.setGeometry(QtCore.QRect(260, 320, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player.setFont(font)
        self.player.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.player.setObjectName("player")
        self.exit = QtWidgets.QLabel(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(730, 20, 55, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QLabel {\n"
"background:none;\n"
"}\n"
"QLabel::hover {\n"
"background:none;\n"
"color:white;\n"
"}")
        self.exit.setAlignment(QtCore.Qt.AlignCenter)
        self.exit.setObjectName("exit")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Game Bầu Cua Online - New Room - PL1"))
        self.title.setText(_translate("Main", "TẠO PHÒNG MỚI"))
        self.credit.setText(_translate("Main", "Game made by MHP. You can buy me a cup of coffee through https://www.buymeacoffee.com/py.hacker.hieu, thank you very much."))
        self.description.setText(_translate("Main", "Bạn muốn làm nhà cái hay người chơi?"))
        self.host.setText(_translate("Main", "Nhà cái"))
        self.player.setText(_translate("Main", "Người chơi"))
        self.exit.setText(_translate("Main", "X"))