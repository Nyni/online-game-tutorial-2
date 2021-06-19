import socket
from _thread import *
import sys

server = "10.0.0.21"
port = 5556

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates socket, AF INET is IPv4

try:

    s.bind((server,port))

except socket.error as e:
    str(e)
    print("Error:", e)

s.listen(2) #opens the port, specifies number.

print("Waiting fotr connection server started")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]




def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())

            pos[player] = data


            #reply = data.decode("utf-8")

            if not data:
                print("Disconnect")
                break


            else:

                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]


                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))

        except:
            break
    print("Lost connection")
    conn.close



currentPlayer = 0 #every time we get a new connetion, we add a new one

while True:

    conn, addr = s.accept() #conn is what's connected, addr is IP address
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer +=1
