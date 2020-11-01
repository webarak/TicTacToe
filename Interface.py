from Client import Client

c = Client()
print("hello you are in the game")

while True:
    try:
        c.Send(input("enter row and col with space between"))
        for i in range(4):
            data = c.Recieve()
            if (data != 'ack'):
                print(data)
            while (data == "again"):
                c.Send(input("enter row and col with space between"))
                data = c.Recieve()
        if (data == '0 won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' or data == 'x won!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'):
            break
    except:
        print("0 won!")
        break

c.Colse_Socket()
