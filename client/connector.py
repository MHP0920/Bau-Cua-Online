import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "8.tcp.ngrok.io"
        self.port = 18136
        self.addr = (self.server, self.port)
        self.client.settimeout(2)
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*2))
        except:
            pass
    def send(self, data):
        try:
            self.client.send(data)
            return pickle.loads(self.client.recv(2048*2))
            
        except socket.error as e:
            print(e)
    def set_host(self, host):
        self.server = host
        self.addr = (self.server, self.port)
    def set_port(self, port):
        self.port = port
        self.addr = (self.server, self.port)
    def flush(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
