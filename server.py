# ------- Bolierplate Code Start -----


import socket
from  threading import Thread
import time
IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
clients = {}
BUFFER_SIZE=4096

def handle_show_list(client) : 
    print("CLIENT IS " , client)
    global clients
    counter=0
    for c in clients:
        counter+=1
        client_addr=clients[c]["addr"][0]
        connected_with=clients[c]["connected_with"]
        msg=""
        if (connected_with) : 
            msg=f"{counter},{c},{client_addr},connected with {connected_with},tiul,\n "
        else :
            msg=f"{counter},{c},{client_addr},Available,tiul,\n "

        client.send(msg.encode())
        time.sleep[1]



def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client, addr)
        client_name=client.recv(4096).decode().lower()
        clients[client_name]={
            "client" : client,
            "addr" : addr,
            "connected_with" : "",
            "file_name" : "",
            "file_size" : 4096
        }
        print(clients)
        print(f'Connection established with {client_name} : {addr}')
        Thread(target=handleClient,args=(client,client_name)).start()

def handle_messages(client,msg,client_name) :
    if (msg=='show list'):
        handle_show_list(client)

def handleClient(client,client_name) :
    wlcmmsg="Welcome You are Now Connected to the server \n Click on refresh to see all active Users \n Select the User and start Chatting by clicking on connect Button" 
    client.send(wlcmmsg.encode())
    
    while True:
        try:
            print("checking",clients)
            BUFFER_SIZE=clients[client_name]["file_size"]

            chunk=client.recv(BUFFER_SIZE)
            print("checking chunk",chunk.decode())
            msg=chunk.decode()
            if msg :
                handle_messages(client,msg,client_name)
            print(msg)
        except :
            pass




def setup():
    print("\n\t\t\t\t\t\t IP MESSENGER \n")

    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER


    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup_thread = Thread(target=setup)           #receiving multiple messages
setup_thread.start()

# ------ Bolierplate Code End -----------
