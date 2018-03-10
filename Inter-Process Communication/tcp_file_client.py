import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

f = open("catatan.txt", "rb")
data = f.read(1024)
while (data):
    s.send(data)
    data = f.read(1024)
f.close()
s.shutdown(socket.SHUT_WR)
print("File berhasil dikirim!")
print(s.recv(1024).decode())
s.close()
