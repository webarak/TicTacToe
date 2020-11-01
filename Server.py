import socket
IP = '127.0.0.1'
Port = 5558
class Server(object):

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((IP, Port))
        self.server_socket.listen(2)
        self.client1_socket, self.client1_address = self.server_socket.accept()
        self.client2_socket, self.client2_address = self.server_socket.accept()

    def GetMassage_From_1(self):
        data = self.client1_socket.recv(1024).decode()
        return data

    def GetMassage_From_2(self):
        data = self.client2_socket.recv(1024).decode()
        return data

    def Send_Massage_To_1(self, data):
        self.client1_socket.send(data.encode())

    def Send_Massage_To_2(self, data):
        self.client2_socket.send(data.encode())

    def Close_Connection(self):
        self.client1_socket.close()
        self.client2_socket.close()

    def Close_Server(self):
        self.server_socket.close()