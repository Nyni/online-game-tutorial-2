import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server = "10.0.0.21"
        self.port = 5556

        #woill automatically get clients address

        self.addr = (self.server,self.port)

        self.pos = self.connect()

    def getPos(self):
        return self.pos


    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()

        # 5 hours in explnation

        except:
            pass
    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()

        except socket.error as e:
            print(e)

