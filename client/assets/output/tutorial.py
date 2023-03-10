# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorial.ui'
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
        self.title.setGeometry(QtCore.QRect(0, 30, 801, 50))
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
        self.description.setGeometry(QtCore.QRect(0, 90, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.description.setFont(font)
        self.description.setStyleSheet("background:none;")
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.credit = QtWidgets.QLabel(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(0, 560, 801, 31))
        self.credit.setStyleSheet("color:white;background-color:none;")
        self.credit.setAlignment(QtCore.Qt.AlignCenter)
        self.credit.setObjectName("credit")
        self.tutorialtb = QtWidgets.QTextBrowser(self.centralwidget)
        self.tutorialtb.setGeometry(QtCore.QRect(40, 190, 731, 351))
        self.tutorialtb.setObjectName("tutorialtb")
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
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Game B???u Cua Online - Opening Page"))
        self.title.setText(_translate("Main", "H?????NG D???N"))
        self.description.setText(_translate("Main", "B???u Cua Online Game"))
        self.credit.setText(_translate("Main", "Game made by MHP. You can buy me a cup of coffee through https://www.buymeacoffee.com/py.hacker.hieu, thank you very much."))
        self.tutorialtb.setHtml(_translate("Main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">B???u Cua Online Game l?? g???</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">B???u Cua Online Game l?? </span><span style=\" font-size:12pt; font-style:italic;\">m???t tr?? ch??i m?? ngu???n m???</span><span style=\" font-size:12pt;\"> ???????c l??m b???i MHP nh??n d???p T???t Qu?? M??o 2023, v???i B???u Cua Online Game b???n c?? th??? ch??i c??ng b???n b??, ch???nh s???a m?? ngu???n ????? tr?? ch??i th??m hay ho???c sinh ?????ng h??n v?? c?? th??? t???o m???t m??y ch??? c???a ri??ng b???n ????? ch??i m???t c??ch ri??ng t??.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">C??ch ch??i</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">V???i giao di???n ????n gi???n, b???n c?? th??? v??o ch??i ngay nh???ng ph??ng ??ang m??? ho???c t??? t???o ph??ng m???i cho b???n v?? ng?????i th??n.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">????? ch??i ngay:</span><span style=\" font-size:12pt;\"> B???n nh???n v??o n??t &quot;T??m ph??ng&quot; ??? giao di???n trang ch??? ????? t??m nh???ng ph??ng ??ang m??? b???ng c??ch nh???p ID ph??ng b???n nh???n ???????c t??? ng?????i ch??i kh??c ho???c ch??? ph??ng.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">??? giao di???n T??m ph??ng, b???n nh???p ID ph??ng c???n v??o v?? nh???n V??o ph??ng</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">????? t???o ph??ng</span><span style=\" font-size:12pt;\">: B???n ???????c l???a ch???n l??m Ng?????i ch??i ho???c Nh?? c??i. V???i vi???c l??m ng?????i ch??i, ph??ng ???? s??? m???c ?????nh Nh?? c??i l?? bot v?? s??? t??? ?????ng ch??i n???u ????? ng?????i ch??i. N???u b???n ch???n Nh?? c??i, ph??ng ???? s??? ???????c t???o d?????i d???ng 0 ng?????i ch??i trong ph??ng v?? b???n c?? quy???n b???t ?????u ch??i khi c?? ??t nh???t 1 ng?????i ch??i.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sau khi ch???n l??m Ng?????i ch??i ho???c Nh?? c??i, b???n s??? ???????c y??u c???u cung c???p T??n ph??ng v?? S??? ng?????i ch??i t???i ??a trong 1 ph??ng. Hi???n t???i tr?? ch??i ch??? h??? tr??? t???i ??a 20 ng?????i trong 1 ph??ng, b???n c?? th??? ch???nh s???a gi???i h???n ??? m??y ch??? c???a ri??ng b???n. ID c???a ph??ng s??? ???????c t???o ng???u nhi??n v?? kh??ng b??? tr??ng v???i ph??ng kh??c.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sau khi ???? t???o ph??ng ho???c v??o ph??ng, b???n s??? ???????c chuy???n ?????n ph??ng ch??? ????? ch??? t???t c??? ng?????i ch??i s???n s??ng ho???c ????? ch??? ????? ng?????i trong ph??ng n???u Nh?? c??i ph??ng c???a b???n l?? bot. </span><span style=\" font-size:12pt; font-weight:600;\">N???u b???n mu???n chia s??? ID cho ng?????i ch??i kh??c, h??y click v??o ch??? &quot;ID: (ID c???a b???n)&quot; g??c tr??n c??ng b??n ph???i, app s??? t??? ?????ng copy cho b???n.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Khi t???t c??? ???? s???n s??ng v?? ph??ng b???t ?????u ch??i, b???n s??? ???????c chuy???n ?????n trang l???a ch???n, s??? c?? 6 l???a ch???n l?? B???u, Cua, T??m, C??, G??, H??? theo ki???u ch??i ti??u chu???n, l??u ?? r???ng m???i con v???t ch??? ???????c ch???n 1 l???n. </span><span style=\" font-size:12pt; font-style:italic;\">N???u b???n l?? Nh?? c??i, b???n s??? kh??ng ???????c ch???n m?? vi???c c???a b???n l?? ng???i ?????i ng?????i ch??i kh??c ch???n v?? b???t ?????u tung x??c x???c.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sau khi ch???n b???n h??y nh???n Kh??a, l??c n??y ph??ng s??? ?????i ?????n khi t???t c??? ?????u kh??a th?? m???i b???t ?????u tung x??c x???c.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Khi ???? ch???n xong b???n s??? ???????c chuy???n ?????n trang tung x??c x???c, h??nh 2D c???a x??c x???c ???????c tung s??? hi???n tr??n m??n h??nh sau ??t gi??y v?? c??? ch??? c???a ch??ng, b???n s??? ???????c bi???t m??nh th???ng hay thua v?? s??? ti???n (MHPoint) c???a b???n s??? ???????c c???ng ho???c gi???m t??? ?????ng. N???u b???n l?? Nh?? c??i, s??? ti???n b???n nh???n ???????c s??? l?? s??? ti???n thua c???a ng?????i ch??i v?? ng?????c l???i, s??? ti???n m???t c???a b???n s??? l?? s??? ti???n th???ng c???a ng?????i ch??i.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sau khi nh???n ???????c k???t qu???, n???u b???n mu???n ch??i ti???p c?? th??? nh???n v??o n??t Ch??i l???i ??? g??c tr??i cu???i m??n h??nh, n??t n??y gi???ng nh?? n??t S???n s??ng, s??? y??u c???u t???t c??? ng?????i ch??i ?????u nh???n th?? m???i b???t ?????u v??n m???i. N???u b???n kh??ng mu???n ch??i n???a, c?? th??? nh???n n??t &quot;X&quot; ??? g??c tr??n c??ng b??n ph???i m??n h??nh, l??c n??y b???n s??? ???????c t??? ?????ng chuy???n v??? m??n h??nh ch??nh.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Nh???ng Quy ?????c</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ti???n t??? s??? c?? k?? hi???u l?? MHPoint v?? kh??ng th??? ?????i qua ti???n th???t v?? ng?????c l???i.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Tr?? ch??i kh??ng y??u c???u b???n cung c???p th??ng tin nh???y c???m l??n tr?? ch??i v?? b???n ???????c khuy???n kh??ch kh??ng n??n tung th??ng tin nh???y c???m c???a m??nh l??n tr?? ch??i b???ng b???t k?? gi?? n??o.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">M???i th??ng tin v??? ng?????i ch??i tr??n tr?? ch??i ?????u c?? th??? thay ?????i trong t???p tin customize.json, b???n c?? th??? thay ?????i t??y th??ch.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">S??? ti???n c???a b???n s??? ???????c l??m m???i sau khi b???n tho??t ph??ng ch??i g???n nh???t, k??? c??? khi s??? MHPoint c???a b???n v??? con s??? 0.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">M??y ch??? ???????c cung c???p b???i MHP mi???n ph?? cho ng?????i d??ng v?? s??? kh??ng y??u c???u b???n cung c???p b???t k?? kho???n chi ph?? n??o, MHP ch??? mong c??c b???n s??? ti???p t???c ???ng h??? (M???t c???c cafe ho???c chia s??? r???ng r??i) ????? nh??m c?? th??? ti???p t???c ph??t tri???n.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">B???n c?? th??? t???o m??y ch??? c???a ri??ng m??nh n???u b???n th???y m??y ch??? public ch??a ???????c t???t, nh??ng mong b???n s??? kh??ng x??a d??ng Credit c???a b???n m??nh v?? c??ng s???c c???a c??? nh??m b??? ra l?? kh?? nhi???u ????</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">C??c b???n c?? th??? ????ng g??i ???ng d???ng th??nh t???p tin .exe, nh??ng nh??m m??nh </span><span style=\" font-size:12pt; font-weight:600;\">s??? kh??ng ch???u tr??ch nhi???m</span><span style=\" font-size:12pt;\"> v???i nh???ng h??nh vi ch??n m?? ?????c v??o t???p tin .exe v?? chia s??? d?????i danh ngh??a l?? ???ng d???ng c???a b???n m??nh. Tr?? ch??i c???a b???n m??nh l?? ho??n to??n m?? ngu???n m??? v?? s??? lu??n lu??n (kh?? ch???c) l?? nh?? v???y.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">M???c ????ch c???a tr?? ch??i n??y l?? ????? gi???i tr?? v???i gia ????nh v?? b???n b?? nh???ng ng??y T???t, vui l??ng kh??ng l???i d???ng ????? tr???c l???i c?? nh??n.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Official Game Link</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">B???n m???i nh???t c???a tr?? ch??i s??? lu??n ???????c c???p nh???t tr??n trang Github c???a MHP0920.</span></p></body></html>"))
        self.exit.setText(_translate("Main", "X"))