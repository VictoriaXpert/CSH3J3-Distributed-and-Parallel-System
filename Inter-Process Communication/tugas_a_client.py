import socket               
 
s = socket.socket()         
port = 12345               
s.connect(('192.168.43.135', port))
print (s.recv(1024).decode())
s.close() 