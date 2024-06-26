# Server.py

#           dabhi Dhruvi R
#           task 5
from socket import *
import time
localhost = '127.0.0.1'
port = 91

# Using TCP/IP 

server = socket(AF_INET,SOCK_STREAM)
server.bind((localhost,port))
server.listen(1)
print(f"Server Is listening on port numbet {port}")

# Waiting FOr The Connection
connect,address = server.accept()
print(f"Connected by {address}")

#with time
timeright = time.ctime()
connect.send(bytes('Hello Client'+  timeright,'utf-8'))
print("Hello Message is Send ☑")

try:
    while True:
# Read The Data
        read = connect.recv(1024).decode()
        if not read:
            break
        
        print('Clinet Message:  ',read)
        # If client ask about how are you?
        if "bye" in read.lower():
            response_to_client = "Goodbye! 🖐"
            connect.send(bytes(response_to_client,'utf-8'))
            print("Response Message is send")
            break
        elif "how are you" in read.lower():
            response_to_client = "I am fine, thank you! How can I assist you further?"
        elif "date" in read.lower():
            response_to_client = f"{time.strftime('%Y-%m-%d')}"
        else:
            response_to_client = (f"Server Receive Client Message   {read}  ")
            
        connect.send(bytes(response_to_client,'utf-8'))
        print('Response Send To Clinet')
except Exception as e:
    print('Error ',e)

finally:
    connect.close()
    print("Connection Close")
    server.close()
    
    """client code
    # Client
from socket import *
import time

localhost = '127.0.0.1'
port = 91
client = socket(AF_INET,SOCK_STREAM)

# Now We COnnect TO The Server 
try:
    client.connect((localhost,port))
    print(f'Client Is connected to the server at port number{port}')

# Rec Data
    RecData = client.recv(1024).decode()
    print('server:',RecData)



    client.send(bytes('Hello Server'+  time.ctime(),'utf-8'))
    print('Hello Message is send to server')
        
    while True:
        input_user = input("Client:    ")
        client.send(bytes(input_user,'utf-8'))
        
        if input_user.lower() == 'bye':
            print('Bye !🖐 Ending the Chat')
            break
        # Response From Server
        response_from_Server = client.recv(1024).decode()
        print('Server:  ',response_from_Server)
        
except Exception as e:
    print('Error ',e)
finally:
    
    client.close()
    print("Connection Closed")"""