# -*- coding: utf-8 -*-

import socket
from _thread import *
import pickle
import random
import string


server = "127.0.0.1"
port = 8080

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
                "playername_randomid": {"balance": 0, "chosen": [], "ingame": False}
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
            if not any(not x['ingame'] for x in list(list_of_rooms[roomid]['players'].values())) and list_of_rooms[roomid]['roomstatus'] == 'waiting' and len(list(list_of_rooms[roomid]['players'].values())) == list_of_rooms[roomid]['total']:
                list_of_rooms[roomid]['roomstatus'] = 'choosing'
            elif not any(not x['chosen'] for x in list(list_of_rooms[roomid]['players'].values())) and list_of_rooms[roomid]['roomstatus'] == 'choosing':
                list_of_rooms[roomid]['roomstatus'] = 'playing'
            elif list_of_rooms[roomid]['result'] and list_of_rooms[roomid]['roomstatus'] == 'playing':
                list_of_rooms[roomid]['roomstatus'] = 'ending'
            elif not any(x['chosen'] for x in list(list_of_rooms[roomid]['players'].values())) and list_of_rooms[roomid]['roomstatus'] == 'ending':
                list_of_rooms[roomid]['result'] = []
                list_of_rooms[roomid]['roomstatus'] = 'waiting'
        except Exception as e:
            print(e)
        return list_of_rooms[roomid]['roomstatus']
    def generate_result(self, roomid):
        result = [random.choice(self.availresult) for _ in range(3)]
        list_of_rooms[roomid]['result'] = result
        return result

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
            current = 1
        conn.sendall(pickle.dumps({"status": status, 'roomid': roomid, 'roomname':  roomname, 'total': total, 
        'current': current}))
        
        #username = returned_info[1];  roomname = returned_info[3]; balance = returned_info[4]; ishost = returned_info[5]; iscreatingroom = returned_info[6]; total = returned_info[7]
        # Assign connected
        connected[username] = conn
        print("User", username, 'connected to server.')
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
                list_of_rooms[roomid]["players"] = {username: {'balance': balance, "chosen": [], "ingame": False}}
            print("User", username, "created room for", roomname + '. Room ID:', roomid)
        else:
            if len(list(list_of_rooms[roomid]['players'].values())) < list_of_rooms[roomid]['total'] and list_of_rooms[roomid]['roomstatus'] == 'waiting':
                list_of_rooms[roomid]["players"][username] = {'balance': balance, "chosen": [], "ingame": False}
                print("User", username, "joined room", roomname + '. Room ID:', roomid + ". Current:", len(list(list_of_rooms[roomid]['players'].values())))
            else:
                print("Rejected user", username, 'to join the experiment, status: Room is full or room is in game. ID:', roomid)
                conn.sendall(str.encode("Trò chơi đã bắt đầu hoặc đã đủ số người chơi."))
                conn.close()
                # Remove user from server
                try:
                    del connected[username]
                except:
                    pass
                return
        while True:
            try:
                data = pickle.loads(conn.recv(4096))

                if roomid in list(list_of_rooms.keys()):
                    if not data:
                        break
                    else:
                        try:
                            if data['status'] == "ready":
                                list_of_rooms[roomid]['players'][username]["ingame"] = True
                                conn.sendall(pickle.dumps({'status': self.features.get_status(roomid)}))
                            elif data['status'] == 'unready':
                                if self.features.get_status(roomid) == 'waiting':
                                    list_of_rooms[roomid]['players'][username]["ingame"] = False
                                conn.sendall(pickle.dumps({'status': self.features.get_status(roomid)}))
                            elif data['status'] == 'status':
                                conn.sendall(pickle.dumps({'status': self.features.get_status(roomid)}))
                            elif data['status'] == 'reset':
                                if self.features.get_status(roomid) == 'ending' or self.features.get_status(roomid) == 'waiting':
                                    list_of_rooms[roomid]['players'][username]['ingame'] = False
                                    list_of_rooms[roomid]['players'][username]['chosen'] = []

                                    self.features.get_status(roomid)
                                    # Ask permission to resubmit new balance
                                    conn.sendall(pickle.dumps({'status': "neednewbalance"}))
                                else:
                                    conn.sendall(pickle.dumps({'status': "rejected"}))
                            elif data['status'] == 'result':
                            
                                if self.features.get_status(roomid) == 'playing':
                                    result = self.features.generate_result(roomid)
                                    list_of_rooms[roomid]['result'] = result
                                    conn.sendall(pickle.dumps({"status": "accepted", "data": result}))
                                else:
                                    conn.sendall(pickle.dumps({"status": "accepted", "data": list_of_rooms[roomid]['result']}))
                            elif data['status'] == 'resubmit':
                                balance = data['balance']
                                if self.features.check_info("tempcheck", roomid, roomname, balance, False, False, total)[0] == False:
                                    print("Reject connection from user", username, 'to server. Status: Balance not valid')
                                    conn.sendall(pickle.dumps({"status": "failed", "message": "Unvalid balance"}))
                                    conn.close()
                                    return
                                else:
                                    conn.sendall(pickle.dumps({"status": "accepted"}))
                            elif data['status'] == 'chose':
                                # Get user chosen
                                if self.features.get_status(roomid) != 'choosing':
                                    conn.sendall(pickle.dumps({"status": "rejected"}))
                                elif not list_of_rooms[roomid]['players'][username]['chosen']:
                                    list_of_rooms[roomid]['players'][username]['chosen'] = data['chosen']
                                    conn.sendall(pickle.dumps({"status": "accepted"}))
                                else:
                                    conn.sendall(pickle.dumps({"status": "rejected"}))
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
                break
        try:
            print("Rejected the connection from user", username, 'to the server, status: Player disconnected. ID:', roomid)
            del list_of_rooms[roomid]['players'][username]
            
        except: pass
        if len(list(list_of_rooms[roomid]['players'].values())) <= 0 or ishost:
            del list_of_rooms[roomid]
            print("Clearing room", roomname, ", status: Room have no player(s) or the host left. ID:", roomid)
        conn.close()
Server()