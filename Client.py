import socket

IP = '127.0.0.1'
Port = 5558

class Client(object):
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((IP, Port))

    def Send(self, data):
        self.client.send(data.encode())

    def Recieve(self):
        data = self.client.recv(1024).decode()
        return data

    def Colse_Socket(self):
        self.client.close()

    def IsOpen(self):
        try:
            self.client.send('ack').encode()
            return True
        except:
            return False
