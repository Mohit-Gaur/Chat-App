import socket
import threading # manages differect threads (Threads means instances we use this lib for our msg handling stuff)
import sys

HEADER = 64

FORMAT = "utf - 8"
PORT = 5050 #defing a port for the server to bind to
DISCONNECT_MSG = "!DISCONNECT"
#defining the server ip address

##SERVER = "192.168.0.101"
  
# another way to assign ip address to the server is by :- 
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
NAME = ""

def handle_client(conn,addr):
    NAME = conn.recv(2048).decode(FORMAT)
    print(f"[NEW CONNECTION] {addr} {NAME} connected.. ")
    connected = True
    while connected:
        #msg_length = conn.recv(HEADER).decode(FORMAT)
        #if msg_length != ' ':
        #msg_length = int(msg_length)
        msg = conn.recv(2048).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        print(f"{NAME} -->> {msg}")
        conn.send("Message Received!".encode(FORMAT))
     
    print(f"[DISCONNECTING] Closing connection with {addr}")
    print(f"Number of Active connections :- [{threading.activeCount()-1}]")
    conn.close()
         
        

def start():
    server.listen()
    print(f"[LISTENING] The server is Listening on {SERVER} ")
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn,addr))
        thread.start()
        print(f"[NUMBER OF ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()        
