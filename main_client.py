import socket
import threading
from tkinter import *
#import tkinter as tk

# root = tk.Tk()

# NAME = ""
# SERVER = ""

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HEADER = 64
FORMAT = "utf - 8"
PORT = 5050 #defing a port for the server to bind to
DISCONNECT_MSG = "!DISCONNECT"

class Window1(Frame):
    # NAME = ""
    # SERVER = ""

    def __init__(self, parent):
       Frame.__init__(self, parent)
       self.parent = parent
       self.initialize()
       self.registration()


    def initialize(self):
    
        self.parent.title("Chat App")
        self.parent.geometry("305x305")     #defining the dimension of the window
        self.parent.minsize(305,305)
        self.parent.maxsize(305,305)
        self.parent.configure(bg='blue')   
    
    def destroyWidgets(self):
        self.NameEntry.destroy()
        self.NameLabel.destroy()
        self.IPEntry.destroy()
        self.IPLabel.destroy()
        self.send_btn.destroy()
        self.quit_btn.destroy()

    def sendDetails(self):
            #print(frame.NameEntry)
        NAME = self.NameEntry.get()
        SERVER = self.IPEntry.get()
        #SERVER = "192.168.56.1"
        Window2.registration(self,NAME,SERVER)
        self.destroyWidgets()
        run = Window2(root)

    def registration(self):
        

        #self.NameVar = StringVar()
        self.NameLabel = Label(self.parent, text="Name:-",padx=1,pady=2,bg='blue',fg='white',relief=FLAT)
        #self.NameVar.set("Name :- ")
        self.NameLabel.place(x=0,y=50,width=70,height=30)
        self.NameEntry = Entry(self.parent)
        self.NameEntry.place(x=65,y=50,width=230,height=30)

        #self.IPVar = StringVar() 
        self.IPLabel = Label(self.parent, text="Server:- ",padx=1,pady=2,bg='blue',fg='white',relief=FLAT)
        #self.IPVar.set("Server :- ")
        self.IPLabel.place(x=0,y=100,width=70,height=30)
        self.IPEntry = Entry(self.parent)
        self.IPEntry.place(x=65,y=100,width=230,height=30)  

        self.send_btn = Button(self.parent, text="Enter", width=15, height=2,font = ('Comic sans ms',8,'bold'), bg='black',fg='white',command=lambda:self.sendDetails())
        self.send_btn.place(x=185, y=285//2)

        self.quit_btn = Button(self.parent, text="Quit", width=15, height=2,font = ('Comic sans ms',8,'bold'), bg='black',fg='white',command=quit)
        self.quit_btn.place(x=5, y=285//2)



class Window2(Frame):
    reply = ""
    # client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def __init__(self, parent1):
       Frame.__init__(self, parent1)
       self.parent1 = parent1
       self.initialize()
       self.chatBox()
       #self.registration()


    def initialize(self):
    
        self.parent1.title("ChatRoom")
        self.parent1.geometry("700x550")     #defining the dimension of the window
        self.parent1.minsize(700,500)
        #self.parent.maxsize(700,500)
        self.parent1.configure(bg='red')   
    
        
    
        
    def chatBox(self):
        self.chatEntry = Entry(self.parent1)
       # self.chatEntry.config(state='readonly')
        self.chatEntry.place(x=10,y=10,height=400,width=675)
        self.msgBox = Entry(self.parent1)
        self.msgBox.place(x=10,y=420,height=55,width = 555)
        photo=PhotoImage(file="send.png")
        self.send_btn = Button(self.parent1,font = ('Comic sans ms',8,'bold'), bg='light Green',fg='white',command=lambda:self.sendMsg())
        self.send_btn.config(image=photo,width="60",height="70")

        self.send_btn.place(x=575, y=418)

    #def display(self,answer):
        # self.chatEntry.insert("1.0",self.answer)    
        
    def registration(self,NAME,SERVER):
        
        print(f"{NAME} {SERVER} {PORT}")

        #SERVER = socket.gethostbyname(socket.gethostname())
        #SERVER = "192.168.43.176"
        
        ADDR = (SERVER,PORT)
        print(ADDR)

        # client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        client.connect(ADDR)

        if NAME != "":
            client.send(NAME.encode(FORMAT))

    def sendMsg(self):
        msg = self.msgBox.get()
        if len(msg) != 0:
            self.msgBox.delete(0,END)
            message = msg.encode(FORMAT)  # same as converting the string into bytes.
        # msg_length = len(message)
        # send_length = str(msg_length).encode(FORMAT)
        # send_length += b' ' * (HEADER - len(send_length))
        #client.send(send_length)
        #message = self.chatEntry.get("1.0",END)
            client.send(message)
        #self.reply = client.recv(2048).decode(FORMAT)
            reply = client.recv(2048).decode(FORMAT)
            if reply == "Message Received!":
                self.chatEntry.delete(0,END)
                self.chatEntry.insert(0,f"[SERVER] -->> {reply}\n") 
            else:
                self.chatEntry.delete(0,END)    
                self.chatEntry.insert(0,"Message Not sent!\n") 
            #self.display(self.reply)
        else:
            self.chatEntry.insert(0,f"[SERVER] -->> Please Enter a Message!") 
               
"""
        msg = 'Hello'
        while True:
            if msg != DISCONNECT_MSG:
                #msg = input("Enter Your Msg :- ")
                #self.chatEntry.insert("2.0","Enter Your Message:-")
                #send(msg)
                #send(self.sendDetails1())
                pass
            else:
                print("[DISCONNECTING]....")
                break;
"""                
        


if __name__ == '__main__':

    root = Tk()
    run = Window1(root)
    

root.mainloop()