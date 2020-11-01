from Matrix import Matrix
from Server import Server
import pickle

class Game(object):
    def __init__(self):
        self.board = Matrix(3,3)
        self.server = Server()

    def AddShape(self, value):
        row = 0
        col = 0

        while (True):
            if (value == 'x'):
                data = self.server.GetMassage_From_1().split(' ')
            else:
                data = self.server.GetMassage_From_2().split(' ')
            row = data[0]
            col = data[1]
            if (self.board.__getitem__(int(row), int(col)) != ''):
                if (value == 'x'):
                    self.server.Send_Massage_To_1("again")
                else:
                    self.server.Send_Massage_To_2("again")

            else:
                self.board.__setitem__(int(row), int(col), value)
                if (value == 'x'):
                    self.server.Send_Massage_To_1("ack")
                else:
                    self.server.Send_Massage_To_2("ack")
                return row ,col



    def PlayGame(self):

        counter = 9
        while(True):
            counter-=1
            row, col = self.AddShape('x')
            self.server.Send_Massage_To_2(self.board.__repr__())
            self.server.Send_Massage_To_1(self.board.__repr__())
            if (self.board.CheckRow(int(row), 'x')==1 or self.board.CheckCol(int(col),'x')==1 or self.board.CheckDiagonal('x')==1 or self.board.CheckSeconderyDiagonal('x')):
                self.server.Send_Massage_To_2('x won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                self.server.Send_Massage_To_1('x won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                break
            elif (counter==0):
                self.server.Send_Massage_To_2(
                    'call it even')
                self.server.Send_Massage_To_1(
                    'call it even')
                break
            else:
                    self.server.Send_Massage_To_1("ack")
                    self.server.Send_Massage_To_2("ack")

            counter-=1
            row, col = self.AddShape('0')
            self.server.Send_Massage_To_2(self.board.__repr__())
            self.server.Send_Massage_To_1(self.board.__repr__())
            if (self.board.CheckRow(int(row), '0')==1 or self.board.CheckCol(int(col),'0')==1 or self.board.CheckDiagonal('0')==1 or self.board.CheckSeconderyDiagonal('0')):
                self.server.Send_Massage_To_2(
                    '0 won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                self.server.Send_Massage_To_1(
                    '0 won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                break
            elif(counter==0):
                self.server.Send_Massage_To_2(
                    'call it even')
                self.server.Send_Massage_To_1(
                    'call it even')
                break
            else:
                self.server.Send_Massage_To_1("ack")
                self.server.Send_Massage_To_2("ack")



if __name__ == '__main__':
    G = Game()
    G.PlayGame()
    G.server.Close_Connection()
    G.server.Close_Server()