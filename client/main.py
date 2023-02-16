# -*- coding: utf-8 -*-

from assets.output import openingpage, findroom, newroom_PL1, newroom_PL2, tutorial, playgame, waitingroom, choosing, playgame_host
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
_total = 0
_being = 'player'
_id = ''
_current = 0
_roomname = ''
_status = 'waiting'
_running = False
_runner = True
_server = []
_user = []

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
        global _id, _total, _roomname, _current, _running, _being
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
            elif resp['status'] == 'fulloringame':
                QMessageBox.critical(None, "Rejected", "Phòng đã đủ người hoặc đang trong trò chơi.")
                _connection.flush()
                _connection.connect()
            else:
                _running = True
                _being = 'player'
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
        self.ui.player.clicked.connect(lambda: self.create_room('player'))
        self.ui.host.clicked.connect(lambda: self.create_room('host'))
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
    def create_room(self, being):
        global _being 
        _being = being
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
        global _id, _roomname, _current, _total, _running, _being
        # Connect to network
        try:
            _running = False
            _connection.flush()
            _connection.connect()
            resp = _connection.send(pickle.dumps({"username": _username, "roomname": self.ui.roomname_input.text(), 'balance': _balance, "ishost": False if _being == 'player' else True, 'icr': True, 'total': int(self.ui.maxplayer_input.text())}))
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
        self.current_timer = 0
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
            resp = _connection.send(pickle.dumps({"status": "lock"}))
            self.current_timer = start_loop(1, self.loop, self.current_timer)
        except Exception as bug:
            print(bug)
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
        self.ui.bau.setEnabled(False);self.ui.cua.setEnabled(False);self.ui.tom.setEnabled(False);self.ui.ca.setEnabled(False);self.ui.ho.setEnabled(False);self.ui.ga.setEnabled(False)
    def choose(self, chose, env=None):
        global _chosen
        _chosen.append(chose)
        resp = _connection.send(pickle.dumps({"status": "chose", 'chosen': [chose]}))
    def loop(self):
        if _status == 'playing' or _status == 'ending':
            self.ui.lock.setText("Khóa")
            self.ui.lock.setEnabled(True)
            self.ui.bau.setEnabled(True);self.ui.cua.setEnabled(True);self.ui.tom.setEnabled(True);self.ui.ca.setEnabled(True);self.ui.ho.setEnabled(True);self.ui.ga.setEnabled(True)
            self.hide()
            _playgame.flush()
            _playgame.show()
            QTimer.singleShot(100, _playgame.start)
            return
        self.current_timer = start_loop(1, self.loop, self.current_timer)
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
        QTimer.singleShot(1, self.set_text)

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
        QTimer.singleShot(1, self.set_text)
    def flush(self):
        self.ui.firstimg.clear()
        self.ui.secondimg.clear()
        self.ui.thirdimg.clear()
    # Prevent disconnection
    def retrygetresult(self, _times):
        global _server
        if _times < 3:
            try:
                resp = _connection.send(pickle.dumps({"status": "result"}))
                _server_chose = resp['data']
                _server = _server_chose
                return
            except:
                QTimer.singleShot(1000, lambda: self.retrygetresult(_times+1))
        if not _server:
            _server = ["Error"]
        return 
    def start(self):
        global _balance, _chosen, _server
        # Flush server result at start to make sure no wrong result
        _server = []
        # Get result from network
        # Send reset req to network
        try:
            QTimer.singleShot(1, lambda: self.retrygetresult(0))
            while not _server:
                self.update()
                QApplication.processEvents()
            if "Error" in _server:
                QMessageBox.critical(None, "Error", "Không thể nhận kết quả từ máy chủ, vui lòng vào lại phòng.")
                _connection.flush()
                self.flush()
                self.hide()
                _openingpage.show()
                _server = []
                return
            
            QTimer.singleShot(2000, lambda: self._process(_server))
        except Exception as e:
            print(e)
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
    def _process(self, _choices):
        global _server, _chosen, _balance
        self.ui.firstimg.setPixmap(self.convert_dict[_choices[0]])
        self.ui.secondimg.setPixmap(self.convert_dict[_choices[1]])
        self.ui.thirdimg.setPixmap(self.convert_dict[_choices[2]])
        _new_balance = _solve(_chosen, _server, _balance)
        _server = []
        if _new_balance <= 0:
            QMessageBox.critical(None, "God", "Bạn đã hết tiền")
            load_customize()
        else:
            _balance = _new_balance
        _chosen = []
        resp = _connection.send(pickle.dumps({"status": "reset"}))
        if resp['status'] == 'neednewbalance':
            resp = _connection.send(pickle.dumps({"status": "resubmit", 'balance': _balance}))
        self.ui.playagain.setEnabled(True)
    def playagain(self):
        self.ui.playagain.setEnabled(False)
        self.flush()
        self.hide()
        _waitingroom.show()
        _waitingroom.ready()

class PlayGame_Host(QMainWindow):
    def __init__(self):
        super(PlayGame_Host, self).__init__()
        self.ui = playgame_host.Ui_Main()
        self.ui.setupUi(self)
        self.setFixedSize(800, 600)
        self.ui.exit.mousePressEvent = self.returnback
        self.closeEvent = self.normalclose
        QTimer.singleShot(1, self.set_text)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.ui.idroom.setToolTip('Nhấn để copy id')
        self.ui.idroom.mousePressEvent = self.copyid
        self.signals = WorkerSignals()
        self.ui.startgame.clicked.connect(self.start)
        self.current_timer = 0
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
    def flush_button(self):
        self.ui.startgame.setText('Bắt đầu')
        self.ui.startgame.clicked.disconnect()
        self.ui.startgame.clicked.connect(self.start)
        self.ui.listplayer.clear()
    def returnback(self, env):
        global _running
        self.flush_button()
        _running = False
        _connection.flush()
        self.hide()
        _openingpage.show()
    def set_text(self):
        self.ui.roomname.setText("Tên phòng: " + _roomname)
        self.ui.idroom.setText("ID: " + _id)
        self.ui.playercount.setText("Số người chơi: %s/%s" % (_current, _total))
        self.ui.currentbalance.setText("Tiền: %s MHPoint" % str(_balance))
        QTimer.singleShot(1, self.set_text)
    # Prevent disconnection
    def retrygetresult(self, _times):
        global _server
        if _times < 3:
            try:
                resp = _connection.send(pickle.dumps({"status": "result"}))
                if resp['status'] == 'roomnotready':
                    _server = ['Unready']
                    return
                _server_chose = resp['data']
                _server = _server_chose
                self.kill_loop()
                _connection.send(pickle.dumps({"status": "lock"}))
                return
            except:
                QTimer.singleShot(1000, lambda: self.retrygetresult(_times+1))
        if not _server:
            _server = ["Error"]
        return 
    def process(self):
        global _balance, _server, _user
        for _player in _user:
            for k, v in _player.items():
                _new_balance = _solve(v['chosen'], _server, v['balance'])
                _tmp =  _new_balance - v['balance']
                self.ui.listplayer.addItem("> Người chơi: " + k.rsplit('_')[0] + ' đã ' + ("thêm " if _tmp > 0 else "mất ") + str(abs(_tmp)) + " MHPoint vào tài khoản!")
                _balance -= _tmp
        _server = []
        _user = []
        _connection.send(pickle.dumps({"status": "reset"}))
    def start(self):
        global _balance, _server, _user
        # Flush server result at start to make sure no wrong result
        _server = []
        # Get result from network
        # Send reset req to network
        try:
            QTimer.singleShot(1, lambda: self.retrygetresult(0))
            while not _server:
                self.update()
                QApplication.processEvents()
            if "Error" in _server:
                QMessageBox.critical(None, "Error", "Không thể nhận kết quả từ máy chủ, vui lòng vào lại phòng.")
                _connection.flush()
                self.hide()
                _openingpage.show()
                _server = []
                return
            if "Unready" in _server:
                QMessageBox.warning(None, "Warning", "Tất cả người chơi chưa sẵn sàng")
                _server = []
                return
            self.ui.listplayer.addItem("> Đang bắt đầu chơi...")
            _current_timer = QTimer()
            _current_timer.timeout.connect(self.process)
            _current_timer.setSingleShot(True)
            _current_timer.start(1)
            while _current_timer.isActive():
                self.update()
                QApplication.processEvents()
            if _balance <= 0:
                QMessageBox.critical(None, "God", "Bạn đã hết tiền")
                load_customize()
            self.ui.startgame.setText('Chơi lại')
            self.ui.startgame.clicked.disconnect()
            self.ui.startgame.clicked.connect(self.playagain)
        except Exception as e:
            print(e)
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
    def playagain(self):
        self.flush_button()
        self.hide()
        _waitingroom.cancel()
        _waitingroom.show()
    def kill_loop(self):
        if self.current_timer:
            try:
                self.current_timer.stop()
                self.current_timer.deleteLater()
            except:
                pass
    def start_loop(self, time, times=0):
        self.kill_loop()
        self.current_timer = QTimer()
        self.current_timer.timeout.connect(lambda: self.updateinfo(times))
        self.current_timer.setSingleShot(True)
        self.current_timer.start(time)
    def updateinfo(self, _times=0):
        global _user
        if _times < 6:
            try:
                resp = _connection.send(pickle.dumps({"status": "get", "type": "chosen"}))
                if resp['status'] == 'accepted':
                    _user_choice = resp['data']
                    _user = _user_choice
                    self.ui.listplayer.clear()
                    for player in _user:
                        for k,v in player.items():
                            _tmp = {}
                            _tmp_str = str(k).rsplit('_', 1)[0] + ': '
                            for _ in set(v['chosen']):
                                _tmp[_] = v['chosen'].count(_)
                                _tmp_str += _ + " (x" + str(_tmp[_]) + "), "
                            if v['locked']:
                                _tmp_str += '(Đã khóa)'
                            self.ui.listplayer.addItem(_tmp_str)

                    self.start_loop(1000, 0)
                else:
                    self.start_loop(1000, _times+1)
                return
            except Exception as bug:
                print(bug)
                self.start_loop(1000, _times+1)
                return
        self.signals.returntomain.emit(1)
        return 

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
        self.current_timer = 0
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
        kill_loop(self.current_timer)
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
            if resp['status'] == 'roomnotready':
                QMessageBox.warning(None, "Chưa đủ người", "Phòng chưa đủ người để bắt đầu")
                self.ui.ready.setEnabled(True)
                return
            self.current_timer = start_loop(1, self.loop, self.current_timer)
        except:
            QMessageBox.critical(None, "Rejected", "Đã có lỗi xảy ra.")
    def cancel(self):
        kill_loop(self.current_timer)
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
            if _being != 'host':
                _choosing.show()
            else:
                _playgame_host.show()
                _playgame_host.start_loop(1000)
            return
        self.current_timer = start_loop(1, self.loop, self.current_timer)
        
    def set_text(self):
        self.ui.roomname.setText("Tên phòng: " + _roomname)
        self.ui.idroom.setText("ID: " + _id)
        # Check player or host
        self.ui.ready.setText("Bắt đầu" if _being == 'host' else "Sẵn sàng")
      
class WorkerSignals(QObject):
    message = pyqtSignal(str)
    returntomain = pyqtSignal(int)

class UpdateStatus(QRunnable):
    def __init__(self):
        super(UpdateStatus, self).__init__()
        self.signals = WorkerSignals()
    def run(self):
        global _status, _current, _runner, _running
        _retry = 0
        while _runner:
            while _running:
                try:
                    if _retry > 10:
                        _running = False
                        _retry = 0
                        _connection.flush()
                        self.signals.returntomain.emit(1)
                        self.signals.message.emit("Mất kết nối với máy chủ, có thể bạn đã bị kick vì phòng đã bắt đầu, chủ phòng đã rời hoặc đường truyền gặp sự cố")
                        break
                    resp = _connection.send(pickle.dumps({'status': "status"}))
                    _status = resp['status']
                    resp = _connection.send(pickle.dumps({"status": "current"}))
                    _current = resp['status']
                except:
                    _retry += 1
                time.sleep(0.05)
            time.sleep(0.5)
        
def load_customize():
    global _username, _balance, _connection
    
    data = json.loads(open('customize.json', 'r', encoding='utf-8').read())
    if data['host'] == 'default':
        _connection.set_host(_default_host)
    elif data['host'] == 'beta':
        _connection.set_host(_beta_host)
    else:
        _connection.set_host(data['host'])

    if data['port'] == 'default':
        _connection.set_port(_default_port)
    elif data['port'] == 'beta':
        _connection.set_port(_beta_port)
    else:
        _connection.set_port(data['port'])
    _username = data['username']
    _balance = data['balance']

def showerror(message):
    QMessageBox.warning(None, "Error", message)

def rtm(num: int):
    if num:
        # Hide all current
        try:
            #_findroom.hide() #_newroom_pl1.hide() #_newroom_pl2.hide() #_tutorial.hidw()
            _waitingroom.hide()
            _playgame.hide()
            _choosing.hide()
            _playgame_host.hide()
            _openingpage.show()
        except:
            pass

def kill_loop(qtimer: QTimer):
        if qtimer:
            try:
                qtimer.stop()
                qtimer.deleteLater()
            except:
                pass
def start_loop(time, function, qtimer=None):
    kill_loop(qtimer)
    current_timer = QTimer()
    current_timer.timeout.connect(function)
    current_timer.setSingleShot(True)
    current_timer.start(time)
    return current_timer


# Make it global.
_default_host = '6.tcp.ngrok.io'; _beta_host = ''
_default_port = 15179; _beta_port = 5000
app = QApplication(sys.argv)
_openingpage = OpeningPage()
_findroom = FindRoom()
_newroom_pl1 = NewRoom_PL1()
_newroom_pl2 = NewRoom_PL2()
_tutorial = Tutorial()
_playgame = PlayGame()
_playgame_host = PlayGame_Host()
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
_updatestatus.signals.message.connect(showerror)
_updatestatus.signals.returntomain.connect(rtm)
_threadpool.start(_updatestatus)
_openingpage.show()

load_customize()

sys.exit(app.exec_())
