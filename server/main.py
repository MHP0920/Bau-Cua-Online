# -*- coding: utf-8 -*-

import socket
from _thread import *
import pickle
import random
import string
import copy
import time

server = "0.0.0.0"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection, Server Started")

connected = {

} 
'''
{
    'playername_randomid': conn
}
'''
list_of_rooms = {} 
'''
{
    "id": {
            "total": 20,
            "roomname": "",
            "roomstatus": "waiting" || "choosing" || "playing" || "ending"
            "host": "playername_randomid" || "bot",
            "players": {
                "playername_randomid": {"balance": 0, "chosen": [], "ingame": False, "locked": False}
            },
            "result": []
        }
}'''

class Additional:
    def __init__(self) -> None:
        self.availresult = ['Bầu', "Cua", "Tôm", "Cá", "Hổ", "Gà"]
    def random_id(self, length: int) -> str:
        return ''.join([random.choice(string.ascii_letters) for i in range(length)])
    def generate_id(self, username):
        id = username + '_' + self.random_id(10)
        while id in list(connected.keys()):
            id = username + '_' + self.random_id(10)
        return id
    def check_info(self, username, roomid, roomname, balance, ishost, icr, total):
        if not username.replace(' ', '').replace('\n', ''):
            return False,
        if not roomid.replace(' ', '').replace('\n', '') and not icr:
            return False,
        elif not roomid.replace(' ', '').replace('\n', '') and icr:
            roomid = self.random_id(5)
            while roomid in list(list_of_rooms.keys()):
                roomid = self.random_id(5)
        elif roomid.replace(' ', '').replace('\n', '') and icr:
            while roomid in list(list_of_rooms.keys()):
                roomid = self.random_id(5)
        if balance <= 0 or balance >= 10**6:
            return False,
        if not icr and roomid not in list(list_of_rooms.keys()):
            return False,
        if username in list(connected.keys()):
            return False,
        if ishost and not icr:
            return False,
        if (total <= 0 or not total) and icr:
            return False,
        if total > 20:
            return False,
        if not roomname.replace(' ', '').replace('\n', '') and icr:
            return False,
        return True, username, roomid, roomname, balance, ishost, icr, total
    def get_status(self, roomid):
        try:
            if not any(not x['ingame'] for x in list(list_of_rooms[roomid]['players'].values())) and list_of_rooms[roomid]['roomstatus'] == 'waiting' and len(list(list_of_rooms[roomid]['players'].values())) == list_of_rooms[roomid]['total'] and list_of_rooms[roomid]['host'] == 'bot':
                list_of_rooms[roomid]['roomstatus'] = 'choosing'
            elif not any(not x['locked'] for x in list(list_of_rooms[roomid]['players'].values())) and list_of_rooms[roomid]['roomstatus'] == 'choosing' and list_of_rooms[roomid]['host'] == 'bot':
                list_of_rooms[roomid]['roomstatus'] = 'playing'
            elif list_of_rooms[roomid]['result'] and list_of_rooms[roomid]['roomstatus'] == 'playing' and list_of_rooms[roomid]['host'] == 'bot':
                list_of_rooms[roomid]['roomstatus'] = 'ending'
            elif not any(x['chosen'] for x in list(list_of_rooms[roomid]['players'].values())) and list_of_rooms[roomid]['roomstatus'] == 'ending' and list_of_rooms[roomid]['host'] == 'bot':
                list_of_rooms[roomid]['result'] = []
                list_of_rooms[roomid]['roomstatus'] = 'waiting'
        except Exception as e:
            print(e)
        return list_of_rooms[roomid]['roomstatus']
    def generate_result(self, roomid):
        result = [random.choice(self.availresult) for _ in range(3)]
        list_of_rooms[roomid]['result'] = result
        return result
    def remove_user(self, username):
        try:
            connected[username].close()
            del connected[username]
        except:
            pass
class Server:
    def __init__(self):
        self.features = Additional()
        while True:
            conn, addr = s.accept()
            start_new_thread(self.threaded_client, (conn,))
    def threaded_client(self, conn: socket.socket):
        global connected, list_of_rooms
        conn.sendall(pickle.dumps({"status": "accepted"}))
        # Get info
        data = pickle.loads(conn.recv(4096))
        status = 'rejected'
        try:
            username = self.features.generate_id(data["username"])
            try:
                roomid = data['roomid']
            except:
                roomid = ''
            balance = data['balance']
            ishost = bool(data['ishost'])
            iscreatingroom = bool(data['icr'])
            try:
                total = data['total']
                roomname = data['roomname']
            except:
                total = 0
                roomname = ''
        except:
            print("Info not reachable")
            conn.sendall(pickle.dumps({"status": status}))
            conn.close()
            return
        # Check info
        returned_info = self.features.check_info(username, roomid, roomname, balance, ishost, iscreatingroom, total)
        if returned_info[0] == False:
            print("Reject connection from user", username, 'to server. Status: Not enough info or info have some problems')
            conn.sendall(pickle.dumps({"status": status}))
            conn.close()
            return
        status = 'accepted'
        roomid = returned_info[2]
        if not iscreatingroom:
            roomname = list_of_rooms[roomid]['roomname']
            total = list_of_rooms[roomid]['total']
            current = len(list(list_of_rooms[roomid]['players'].values()))+1
        else:
            if not ishost:
                current = 1
            else:
                current = 0
        
        #username = returned_info[1];  roomname = returned_info[3]; balance = returned_info[4]; ishost = returned_info[5]; iscreatingroom = returned_info[6]; total = returned_info[7]
        # Assign connected
        connected[username] = conn
        print("User", username, 'connected to server.')
        def acp_message():
            conn.sendall(pickle.dumps({"status": status, 'roomid': roomid, 'roomname':  roomname, 'total': total, 
            'current': current}))
        # Assign room
        if iscreatingroom:
            list_of_rooms[roomid] = {
                "total": total,
                "roomname": roomname,
                "roomstatus": "waiting",
                "host": username if ishost else "bot",
                "players": {},
                "result": []
            }
            if not ishost:
                list_of_rooms[roomid]["players"] = {username: {'balance': balance, "chosen": [], "ingame": False, 'locked': False}}
            print("User", username, "created room for", roomname + '. Room ID:', roomid)
            acp_message()
        else:
            if len(list(list_of_rooms[roomid]['players'].values())) < list_of_rooms[roomid]['total'] and list_of_rooms[roomid]['roomstatus'] == 'waiting':
                list_of_rooms[roomid]["players"][username] = {'balance': balance, "chosen": [], "ingame": False, "locked": False}
                print("User", username, "joined room", roomname + '. Room ID:', roomid + ". Current:", len(list(list_of_rooms[roomid]['players'].values())))
                acp_message()
            else:
                print("Rejected user", username, 'to join the experiment, status: Room is full or room is in game. ID:', roomid)
                conn.sendall(pickle.dumps({"message": "Trò chơi đã bắt đầu hoặc đã đủ số người chơi.", 'status': "fulloringame"}))
                conn.close()
                # Remove user from server
                self.features.remove_user(username)
                return
        while True:
            try:
                data = pickle.loads(conn.recv(4096))
                _temp_dict = copy.deepcopy(list_of_rooms)
                if roomid in list(_temp_dict.keys()):
                    if not data:
                        break
                    else:
                        try:
                            if data['status'] == "ready":
                                if not ishost:
                                    list_of_rooms[roomid]['players'][username]["ingame"] = True
                                    conn.sendall(pickle.dumps({'status': self.features.get_status(roomid)}))
                                    
                                else:
                                    # Remove all unready player to start the game
                                    if len(list(list_of_rooms[roomid]['players'].values())) > 0 and any(x['ingame'] for x in list(list_of_rooms[roomid]['players'].values())):
                                        list_of_rooms[roomid]['roomstatus'] = 'choosing'
                                        for key, _player in _temp_dict[roomid]['players'].items():
                                            if _player['ingame'] == False:
                                                try:
                                                    del list_of_rooms[roomid]['players'][key]
                                                    self.features.remove_user(key)
                                                except:
                                                    pass
                                        conn.sendall(pickle.dumps({'status': self.features.get_status(roomid)}))
                                        
                                    else:
                                        conn.sendall(pickle.dumps({'status': "roomnotready"}))
                                        


                                
                            elif data['status'] == 'unready' and not ishost:
                                if self.features.get_status(roomid) == 'waiting':
                                    list_of_rooms[roomid]['players'][username]["ingame"] = False
                                conn.sendall(pickle.dumps({'status': self.features.get_status(roomid)}))
                            elif data['status'] == 'status':
                                conn.sendall(pickle.dumps({'status': self.features.get_status(roomid)}))
                            elif data['status'] == 'reset':
                                if not ishost: # Noted.
                                    list_of_rooms[roomid]['players'][username]['ingame'] = False
                                    list_of_rooms[roomid]['players'][username]['chosen'] = []
                                    list_of_rooms[roomid]['players'][username]['locked'] = False

                                    self.features.get_status(roomid)
                                    # Ask permission to resubmit new balance
                                    conn.sendall(pickle.dumps({'status': "neednewbalance"}))
                                else:
                                    # Wait for all players to get the result
                                    time.sleep(5)
                                    list_of_rooms[roomid]['roomstatus'] = 'waiting'
                                    list_of_rooms[roomid]['result'] = []
                                    conn.sendall(pickle.dumps({'status': "accepted"}))
                            elif data['status'] == 'result':
                                if not ishost and list_of_rooms[roomid]['host'] != 'bot':
                                    # wait a little bit
                                    time.sleep(2)
                                if (self.features.get_status(roomid) == 'playing' and not ishost and list_of_rooms[roomid]['host'] == 'bot') or (not any(not x['locked'] for x in list(list_of_rooms[roomid]['players'].values())) and ishost and not list_of_rooms[roomid]['result']):
                                    result = self.features.generate_result(roomid)
                                    list_of_rooms[roomid]['result'] = result
                                    conn.sendall(pickle.dumps({"status": "accepted", "data": result}))
                                elif (self.features.get_status(roomid) != 'playing' and not ishost and list_of_rooms[roomid]['host'] == 'bot') or (self.features.get_status(roomid) == 'playing' and not ishost and list_of_rooms[roomid]['host'] != 'bot'):
                                    conn.sendall(pickle.dumps({"status": "accepted", "data": list_of_rooms[roomid]['result']}))
                                else:
                                    conn.sendall(pickle.dumps({"status": "roomnotready"}))

                            elif data['status'] == 'resubmit' and not ishost:
                                balance = data['balance']
                                if self.features.check_info("tempcheck", roomid, roomname, balance, False, False, total)[0] == False:
                                    print("Reject connection from user", username, 'to server. Status: Balance not valid')
                                    conn.sendall(pickle.dumps({"status": "failed", "message": "Unvalid balance"}))
                                    conn.close()
                                    self.features.remove_user(username)
                                    return
                                else:
                                    conn.sendall(pickle.dumps({"status": "accepted"}))
                            elif data['status'] == 'chose':
                                # Get user chosen
                                if self.features.get_status(roomid) != 'choosing':
                                    conn.sendall(pickle.dumps({"status": "rejected"}))
                                else:
                                    list_of_rooms[roomid]['players'][username]['chosen'].extend(data['chosen'])
                                    conn.sendall(pickle.dumps({"status": "accepted"}))
                            elif data['status'] == 'lock':
                                if not ishost:
                                    list_of_rooms[roomid]['players'][username]['locked'] = True
                                    conn.sendall(pickle.dumps({"status": "accepted"}))
                                else:
                                    if not any(not x['locked'] for x in list(list_of_rooms[roomid]['players'].values())):
                                        list_of_rooms[roomid]['roomstatus'] = 'playing'
                                        conn.sendall(pickle.dumps({"status": "accepted"}))
                                    else:
                                        conn.sendall(pickle.dumps({"status": "roomnotready"}))
                                        
                            elif data['status'] == 'get':
                                if data['type'] == 'chosen' and ishost:
                                    _lst = [{k: v} for k, v in list_of_rooms[roomid]['players'].items()]
                                    conn.sendall(pickle.dumps({'status': 'accepted', 'data': _lst}))
                                else:
                                    conn.sendall(pickle.dumps({'status': "rejected"}))

                            elif data['status'] == 'current':
                                conn.sendall(pickle.dumps({"status": len(list(list_of_rooms[roomid]['players'].values()))}))
                            else:
                                conn.sendall(pickle.dumps({"status": "unknown"}))
                        except Exception as e:
                            print(e)
                            conn.sendall(pickle.dumps({"status": "unknown"}))
                else:
                    break
            except:
                self.features.remove_user(username)
                break
        try:
            print("Rejected the connection from user", username, 'to the server, status: Player disconnected. ID:', roomid)
            del list_of_rooms[roomid]['players'][username]
            
        except: pass
        try:
            if (len(list(list_of_rooms[roomid]['players'].values())) <= 0 and ishost == 'bot') or ishost:
                for key, _player in _temp_dict[roomid]['players'].items():
                    try:
                        self.features.remove_user(key)
                    except:
                        pass
                del list_of_rooms[roomid]
                print("Clearing room", roomname, ", status: Room have no player(s) or the host left. ID:", roomid)
        except Exception as bug:
            pass
        conn.close()
        self.features.remove_user(username)
Server()