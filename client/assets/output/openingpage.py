# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openingpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main: QtWidgets.QMainWindow):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        Main.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 73, 75, 255), stop:0.997452 rgba(255, 189, 96, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 150, 801, 50))
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
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(0, 220, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.description.setFont(font)
        self.description.setStyleSheet("background:none;")
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.findroom = QtWidgets.QPushButton(self.centralwidget)
        self.findroom.setGeometry(QtCore.QRect(120, 320, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.findroom.setFont(font)
        self.findroom.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.findroom.setObjectName("findroom")
        self.newroom = QtWidgets.QPushButton(self.centralwidget)
        self.newroom.setGeometry(QtCore.QRect(260, 320, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.newroom.setFont(font)
        self.newroom.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.newroom.setObjectName("newroom")
        self.credit = QtWidgets.QLabel(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(0, 560, 801, 31))
        self.credit.setStyleSheet("color:white;background-color:none;")
        self.credit.setAlignment(QtCore.Qt.AlignCenter)
        self.credit.setObjectName("credit")
        self.tutorial = QtWidgets.QPushButton(self.centralwidget)
        self.tutorial.setGeometry(QtCore.QRect(150, 390, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tutorial.setFont(font)
        self.tutorial.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.tutorial.setObjectName("tutorial")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Game Bầu Cua Online - Opening Page"))
        self.title.setText(_translate("Main", "CHÀO MỪNG BẠN ĐẾN VỚI"))
        self.description.setText(_translate("Main", "Bầu Cua Online Game"))
        self.findroom.setText(_translate("Main", "Tìm phòng"))
        self.newroom.setText(_translate("Main", "Tạo phòng mới"))
        self.credit.setText(_translate("Main", "Game made by MHP. You can buy me a cup of coffee through https://www.buymeacoffee.com/py.hacker.hieu, thank you very much."))
        self.tutorial.setText(_translate("Main", "Đọc hướng dẫn"))