#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name=None
listbox=None
textarea=None
labelchat=None
text_message=None

def connect_to_server():
    global SERVER
    global name

    c_name=name.get()
    SERVER.send(c_name.encode())

def showClientsList():
    global SERVER
    global clients
    global listbox

    listbox.delete(0,END)
    SERVER.send("show list".encode("ascii"))

def openChatwin():
    window=Tk()
    window.geometry("520x350")
    window.title("Messenger")
    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    

    namelabel=Label(window,text='Enter Your Name :- ',font=("Algerian",10))
    namelabel.place(x=10,y=8)

    name=Entry(window,width=30,font=("Algerian",10))
    name.place(x=130,y=8)
    name.focus()

    connectserver=Button(window,text='Connect to chat server',bd=1,font=('Algerian',10),command=connect_to_server)
    connectserver.place(x=350,y=6)


    sperator=ttk.Separator(window,orient='horizontal')
    sperator.place(x=10,y=40,relwidth=1,relheight=0.1)

    labelusers=Label(window,text="Active Users:- ",font=("Algerian",10))
    labelusers.place(x=10,y=50)

    listbox=Listbox(window,font=("Algerian",10),height=5,width=67,activestyle="dotbox")
    listbox.place(x=10,y=70)

    connectbtn=Button(window,text='Connect',bd=1,font=("Algerian",10))
    connectbtn.place(x=200,y=160)

    disconnectbtn=Button(window,text='Disconnect',bd=1,font=("Algerian",10))
    disconnectbtn.place(x=350,y=160)

    refreshbtn=Button(window,text="Refresh",font=("Algerian",10),bd=1,command=showClientsList)
    refreshbtn.place(x=435,y=160)

    chatwin=Label(window,text="Chat Window",font=("Algerian",10))
    chatwin.place(x=10,y=180)

    textarea=Text(window,font=("Algerian",10),height=5,width=67)
    textarea.place(x=10,y=200)

    scrollbar2=Scrollbar(textarea)
    scrollbar2.place(relheight=1,relx=1)
    scrollbar2.config(command=listbox.yview)
    
    attach=Button(window,text="Attach And Send",font=('Algerian',10),bd=1)
    attach.place(x=10,y=300)

    filePathLabel=Label(window,text="",fg='blue',font=("Algerian",10))
    filePathLabel.place(x=10,y=330)

    send=Button(window,text="Send",font=('Algerian',10),bd=1)
    send.place(x=200,y=320)

    window.mainloop()

def recv_msg():
    global SERVER
    global BUFFER_SIZE
    while True :
        chunk=SERVER.recv(BUFFER_SIZE)
        print("C",chunk.decode())
        try : 
             if("tiul" in chunk.decode()) :
                 letter_list=chunk.decode().split(",")
                 print(letter_list)
                 listbox.insert(letter_list[0],letter_list[0]+" : " + letter_list[1]+" : " +letter_list[3]+" "+letter_list[5])
             else : 
                 textarea.insert(END,"\n"+chunk.decode('ascii'))
                 textarea.see("end")

        except :
            pass; 
                 
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    recv_thread=Thread(target=recv_msg)
    recv_thread.start()
    openChatwin()


setup()
#-----------Bolierplate Code Start -----

