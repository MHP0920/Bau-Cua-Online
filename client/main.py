# -*- coding: utf-8 -*-

from assets.output import openingpage, findroom, newroom_PL1, newroom_PL2, tutorial, playgame, waitingroom, choosing
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import connector
import json
import pickle
import time
from processor import _solve
import pyperclip

# Make it global.
_roomid = ''
_total = 0
_ishost = False
_icr = False
_being = ''
_id = ''
_current = 0
_roomname = ''
_status = 'waiting'
_running = False
_runner = True


class OpeningPage(QMainWindow):
    def __init__(self):
        super(OpeningPage, self).__init__()
        self.ui = openingpage.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.findroom.clicked.connect(self.findroom)
        self.ui.newroom.clicked.connect(self.newroom)
        self.ui.tutorial.clicked.connect(self._tutorial)
        self.closeEvent = self.normalclose
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
        # Prevent memory leaks
        '''_findroom.close()
        _newroom_pl1.close()
        _newroom_pl2.close()
        _tutorial.close()
        _playgame.close()
        _waitingroom.close()
        _choosing.close()'''
    def findroom(self):
        _findroom.show()
        self.hide()
    def newroom(self):
        _newroom_pl1.show()
        self.hide()
    def _tutorial(self):
        _tutorial.show()
        self.hide()
    
class FindRoom(QMainWindow):
    def __init__(self):
        super(FindRoom, self).__init__()
        self.ui = findroom.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.ui.roomid_input.returnPressed.connect(self.findroom)
        self.ui.joinroom.clicked.connect(self.findroom)
        self.closeEvent = self.normalclose
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
    def returnback(self, env):
        self.hide()
        _openingpage.show()
    def findroom(self, env=None):
        global _id, _total, _roomname, _current, _running
        # Connect to network
        try:
            _running = False
            _connection.flush()
            _connection.connect()
            resp = _connection.send(pickle.dumps({"username": _username, "roomid": self.ui.roomid_input.text(), 'balance': _balance, "ishost": False, 'icr': False}))
            if resp['status'] == 'rejected':
                QMessageBox.critical(None, "Rejected", "Không tìm thấy phòng hoặc thông tin của bạn chưa đủ.")
                _connection.flush()
                _connection.connect()
            else:
                _running = True
                _id = resp['roomid']
                _total = resp['total']
                _roomname = resp['roomname']
                _current = resp['current']
                _waitingroom.show()
                _waitingroom.set_text()
                self.hide()
        except:
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
            _connection.flush()
            try:
                _connection.connect()
            except:
                pass
class Tutorial(QMainWindow):
    def __init__(self):
        super(Tutorial, self).__init__()
        self.ui = tutorial.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.closeEvent = self.normalclose
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
    def returnback(self, env):
        self.hide()
        _openingpage.show()

class NewRoom_PL1(QMainWindow):
    def __init__(self):
        super(NewRoom_PL1, self).__init__()
        self.ui = newroom_PL1.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.ui.player.clicked.connect(self.beaplayer)
        self.closeEvent = self.normalclose
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
    def returnback(self, env):
        self.hide()
        _openingpage.show()
    def beaplayer(self):
        global _being 
        _being = 'player'
        _newroom_pl2.show()
        self.hide()

class NewRoom_PL2(QMainWindow):
    def __init__(self):
        super(NewRoom_PL2, self).__init__()
        self.ui = newroom_PL2.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.ui.createroom.clicked.connect(self.createroom)
        self.closeEvent = self.normalclose
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
    def returnback(self, env):
        self.hide()
        _openingpage.show()
    def createroom(self):
        global _id, _roomname, _current, _total, _running
        # Connect to network
        try:
            _running = False
            _connection.flush()
            _connection.connect()
            resp = _connection.send(pickle.dumps({"username": _username, "roomname": self.ui.roomname_input.text(), 'balance': _balance, "ishost": False, 'icr': True, 'total': int(self.ui.maxplayer_input.text())}))
            if resp['status'] == 'rejected':
                QMessageBox.critical(None, "Rejected", "Thông tin của bạn chưa đủ hoặc máy chủ đang gặp vấn đề.")
                _connection.flush()
                _connection.connect()
            else:
                _running = True
                _id = resp['roomid']
                _total = resp['total']
                _roomname = resp['roomname']
                _current = resp['current']
                _waitingroom.show()
                _waitingroom.set_text()
                self.hide()
        except Exception as e:
            print(e)
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
            _connection.flush()
            try:
                _connection.connect()
            except:
                pass
class Choosing(QMainWindow):
    def __init__(self):
        super(Choosing, self).__init__()
        self.ui = choosing.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.ui.bau.mousePressEvent = lambda x: self.choose('Bầu')
        self.ui.cua.mousePressEvent = lambda x: self.choose('Cua')
        self.ui.tom.mousePressEvent = lambda x: self.choose('Tôm')
        self.ui.ca.mousePressEvent = lambda x: self.choose('Cá')
        self.ui.ga.mousePressEvent = lambda x: self.choose('Gà')
        self.ui.ho.mousePressEvent = lambda x: self.choose('Hổ')
        self.ui.lock.clicked.connect(self.lock)
        self.closeEvent = self.normalclose
        QTimer.singleShot(1000, self.set_text)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.ui.idroom.setToolTip('Nhấn để copy id')
        self.ui.idroom.mousePressEvent = self.copyid
    def copyid(self, env=None):
        pyperclip.copy(_id)
    def lock(self):
        if not _chosen:
            QMessageBox.warning(None, "Failed", "Bạn phải chọn con vật trước khi khóa.")
            return
        self.ui.lock.setText("Bạn đã khóa")
        self.ui.lock.setEnabled(False)
        # Send chosen to network
        try:
            resp = _connection.send(pickle.dumps({"status": "chose", 'chosen': _chosen}))
            QTimer.singleShot(1, self.loop)
        except:
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
        self.ui.bau.setEnabled(False);self.ui.cua.setEnabled(False);self.ui.tom.setEnabled(False);self.ui.ca.setEnabled(False);self.ui.ho.setEnabled(False);self.ui.ga.setEnabled(False)
    def choose(self, chose, env=None):
        global _chosen
        _chosen.append(chose)
    def loop(self):
        if _status == 'playing' or _status == 'ending':
            self.ui.lock.setText("Khóa")
            self.ui.lock.setEnabled(True)
            self.ui.bau.setEnabled(True);self.ui.cua.setEnabled(True);self.ui.tom.setEnabled(True);self.ui.ca.setEnabled(True);self.ui.ho.setEnabled(True);self.ui.ga.setEnabled(True)
            self.hide()
            _playgame.flush()
            _playgame.show()
            QTimer.singleShot(3000, _playgame.start)
            return
        QTimer.singleShot(1000, self.loop)
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        _connection.flush()
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
    def returnback(self, env):
        global _running
        self.ui.lock.setText("Khóa")
        self.ui.lock.setEnabled(True)
        self.ui.bau.setEnabled(True);self.ui.cua.setEnabled(True);self.ui.tom.setEnabled(True);self.ui.ca.setEnabled(True);self.ui.ho.setEnabled(True);self.ui.ga.setEnabled(True)
        _running = False
        _connection.flush()
        self.hide()
        _openingpage.show()
    def set_text(self):
        self.ui.roomname.setText("Tên phòng: " + _roomname)
        self.ui.idroom.setText("ID: " + _id)
        self.ui.playercount.setText("Số người chơi: %s/%s" % (_current, _total))
        self.ui.currentbalance.setText("Tiền: %s MHPoint" % str(_balance))
        QTimer.singleShot(1000, self.set_text)

class PlayGame(QMainWindow):
    def __init__(self):
        super(PlayGame, self).__init__()
        self.ui = playgame.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.closeEvent = self.normalclose
        QTimer.singleShot(1, self.set_text)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.convert_dict = {"Bầu": QPixmap("assets/images/bau.png"),
        "Cua": QPixmap("assets/images/cua.png"),
        "Tôm": QPixmap("assets/images/tom.png"),
        "Cá": QPixmap("assets/images/ca.png"),
        "Hổ": QPixmap("assets/images/ho.png"),
        "Gà": QPixmap("assets/images/ga.png")}
        self.ui.playagain.setEnabled(False)
        self.ui.playagain.clicked.connect(self.playagain)
        self.ui.idroom.setToolTip('Nhấn để copy id')
        self.ui.idroom.mousePressEvent = self.copyid
    def copyid(self, env=None):
        pyperclip.copy(_id)
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
    def returnback(self, env):
        global _running
        _running = False
        self.ui.playagain.setEnabled(False)
        _connection.flush()
        self.hide()
        _openingpage.show()
    def set_text(self):
        self.ui.roomname.setText("Tên phòng: " + _roomname)
        self.ui.idroom.setText("ID: " + _id)
        self.ui.playercount.setText("Số người chơi: %s/%s" % (_current, _total))
        self.ui.currentbalance.setText("Tiền: %s MHPoint" % str(_balance))
        QTimer.singleShot(1000, self.set_text)
    def flush(self):
        self.ui.firstimg.clear()
        self.ui.secondimg.clear()
        self.ui.thirdimg.clear()
    def start(self):
        global _balance, _chosen
        # Get result from network
        # Send reset req to network
        try:
            resp = _connection.send(pickle.dumps({"status": "result"}))
            _server_chose = resp['data']
            self._process(_server_chose)
            _new_balance = _solve(_chosen, _server_chose, _balance)
            if _new_balance <= 0:
                QMessageBox.critical(None, "God", "Bạn đã hết tiền =)))))))")
                load_customize()
            else:
                _balance = _new_balance
            _chosen = []
            resp = _connection.send(pickle.dumps({"status": "reset"}))
            if resp['status'] == 'neednewbalance':
                resp = _connection.send(pickle.dumps({"status": "resubmit", 'balance': _balance}))
            self.ui.playagain.setEnabled(True)
        except Exception as e:
            print(e)
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
    def _process(self, _choices):
        self.ui.firstimg.setPixmap(self.convert_dict[_choices[0]])
        self.ui.secondimg.setPixmap(self.convert_dict[_choices[1]])
        self.ui.thirdimg.setPixmap(self.convert_dict[_choices[2]])
    def playagain(self):
        self.ui.playagain.setEnabled(False)
        self.flush()
        self.hide()
        _waitingroom.show()
        _waitingroom.ready()
class WaitingRoom(QMainWindow):
    def __init__(self):
        super(WaitingRoom, self).__init__()
        self.ui = waitingroom.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.ui.ready.clicked.connect(self.ready)
        self.ui.cancel.clicked.connect(self.cancel)
        self.closeEvent = self.normalclose
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.ui.idroom.setToolTip('Nhấn để copy id')
        self.ui.idroom.mousePressEvent = self.copyid
    def copyid(self, env=None):
        pyperclip.copy(_id)
    def normalclose(self, env=None):
        global _running, _runner
        _running = False
        _runner = False
        self.setEnabled(False)
        while _threadpool.activeThreadCount():
            self.update()
            QApplication.processEvents()
        _threadpool.clear()
        self.close()
    def returnback(self, env):
        global _running
        _running = False
        _connection.flush()
        self.ui.ready.setEnabled(True)
        self.hide()
        _openingpage.show()
    def ready(self):
        # Connect to network
        try:
            self.ui.ready.setEnabled(False)
            resp = _connection.send(pickle.dumps({"status": "ready"}))
            QTimer.singleShot(1, self.loop)
        except:
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
    def cancel(self):
        # Connect to network
        try:
            resp = _connection.send(pickle.dumps({"status": "unready"}))
            self.ui.ready.setEnabled(True)
        except:
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
    def loop(self):
        if _status == 'choosing':
            self.ui.ready.setEnabled(True)
            self.hide()
            _choosing.show()
            return
        QTimer.singleShot(1000, self.loop)
        
    def set_text(self):
        self.ui.roomname.setText("Tên phòng: " + _roomname)
        self.ui.idroom.setText("ID: " + _id)

class UpdateStatus(QRunnable):
    def __init__(self):
        super(UpdateStatus, self).__init__()
    def run(self):
        global _status, _current
        while _runner:
            while _running:
                try:
                    resp = _connection.send(pickle.dumps({'status': "status"}))
                    _status = resp['status']
                    resp = _connection.send(pickle.dumps({"status": "current"}))
                    _current = resp['status']
                except:
                    pass
                time.sleep(1)
            time.sleep(1)
        
def load_customize():
    global _username, _balance, _connection
    data = json.loads(open('customize.json', 'r', encoding='utf-8').read())
    if data['host'] != 'default':
        _connection.set_host(data['host'])
    if data['port'] != 'default':
        _connection.set_port(data['port'])
    _username = data['username']
    _balance = data['balance']

# Make it global.
app = QApplication(sys.argv)
_openingpage = OpeningPage()
_findroom = FindRoom()
_newroom_pl1 = NewRoom_PL1()
_newroom_pl2 = NewRoom_PL2()
_tutorial = Tutorial()
_playgame = PlayGame()
_waitingroom = WaitingRoom()
_choosing = Choosing()
_chosen = []
_balance = 0
_username = ''
_connection = connector.Network()
_threadpool = QThreadPool()
_threadpool.setMaxThreadCount(50)
_updatestatus = UpdateStatus()
_updatestatus.setAutoDelete(True)
_threadpool.start(_updatestatus)
_openingpage.show()

load_customize()

sys.exit(app.exec_())
