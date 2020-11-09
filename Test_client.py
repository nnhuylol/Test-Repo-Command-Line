# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# receive data from the server 
#send message
k = ""
m = ""
while True:
    k=s.recv(1024)
    print (k)
    print ('Mess:')
    m=input()
    s.send(m.encode('utf-8'))
    if (k==b'exit') or (m=='exit'):
        break
    # close the connection 
print('exit')
s.close() 