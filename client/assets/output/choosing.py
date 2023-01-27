# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choosing.ui'
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
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(0, 90, 801, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setAutoFillBackground(False)
        self.status.setStyleSheet("background:none;")
        self.status.setScaledContents(True)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.credit = QtWidgets.QLabel(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(0, 560, 801, 31))
        self.credit.setStyleSheet("color:white;background-color:none;")
        self.credit.setAlignment(QtCore.Qt.AlignCenter)
        self.credit.setObjectName("credit")
        self.currentbalance = QtWidgets.QLabel(self.centralwidget)
        self.currentbalance.setGeometry(QtCore.QRect(510, 490, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.currentbalance.setFont(font)
        self.currentbalance.setStyleSheet("background:none;")
        self.currentbalance.setAlignment(QtCore.Qt.AlignCenter)
        self.currentbalance.setObjectName("currentbalance")
        self.lock = QtWidgets.QPushButton(self.centralwidget)
        self.lock.setGeometry(QtCore.QRect(30, 490, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lock.setFont(font)
        self.lock.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.lock.setObjectName("lock")
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
        self.bau = QtWidgets.QLabel(self.centralwidget)
        self.bau.setGeometry(QtCore.QRect(30, 180, 131, 131))
        self.bau.setText("")
        self.bau.setPixmap(QtGui.QPixmap("assets/images/bau.png"))
        self.bau.setScaledContents(True)
        self.bau.setObjectName("bau")
        self.cua = QtWidgets.QLabel(self.centralwidget)
        self.cua.setGeometry(QtCore.QRect(340, 180, 131, 131))
        self.cua.setText("")
        self.cua.setPixmap(QtGui.QPixmap("assets/images/cua.png"))
        self.cua.setScaledContents(True)
        self.cua.setObjectName("cua")
        self.ca = QtWidgets.QLabel(self.centralwidget)
        self.ca.setGeometry(QtCore.QRect(30, 320, 131, 131))
        self.ca.setText("")
        self.ca.setPixmap(QtGui.QPixmap("assets/images/ca.png"))
        self.ca.setScaledContents(True)
        self.ca.setObjectName("ca")
        self.ga = QtWidgets.QLabel(self.centralwidget)
        self.ga.setGeometry(QtCore.QRect(640, 320, 131, 131))
        self.ga.setText("")
        self.ga.setPixmap(QtGui.QPixmap("assets/images/ga.png"))
        self.ga.setScaledContents(True)
        self.ga.setObjectName("ga")
        self.ho = QtWidgets.QLabel(self.centralwidget)
        self.ho.setGeometry(QtCore.QRect(340, 320, 131, 131))
        self.ho.setText("")
        self.ho.setPixmap(QtGui.QPixmap("assets/images/ho.png"))
        self.ho.setScaledContents(True)
        self.ho.setObjectName("ho")
        self.tom = QtWidgets.QLabel(self.centralwidget)
        self.tom.setGeometry(QtCore.QRect(640, 180, 131, 131))
        self.tom.setText("")
        self.tom.setPixmap(QtGui.QPixmap("assets/images/tom.png"))
        self.tom.setScaledContents(True)
        self.tom.setObjectName("tom")
        self.roomname = QtWidgets.QLabel(self.centralwidget)
        self.roomname.setGeometry(QtCore.QRect(320, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.roomname.setFont(font)
        self.roomname.setStyleSheet("background:none;")
        self.roomname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.roomname.setObjectName("roomname")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Game Bầu Cua Online - In Game - Choosing"))
        self.status.setText(_translate("Main", "Vui lòng chọn con vật bạn muốn đặt cược"))
        self.credit.setText(_translate("Main", "Game made by MHP. You can buy me a cup of coffee through https://www.buymeacoffee.com/py.hacker.hieu, thank you very much."))
        self.currentbalance.setText(_translate("Main", "Tiền còn lại: 0 MHPoint"))
        self.lock.setText(_translate("Main", "Khóa"))
        self.exit.setText(_translate("Main", "X"))
        self.idroom.setText(_translate("Main", "ID:"))
        self.playercount.setText(_translate("Main", "Số người chơi: 0/0"))
        self.roomname.setText(_translate("Main", "Tên phòng:"))