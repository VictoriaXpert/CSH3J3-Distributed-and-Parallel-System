import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

f = open("catatan.txt", "rb")
data = f.read(1024)
while (data):
    s.sendto(data, (UDP_IP, UDP_PORT))
    data = f.read(1024)
f.close()
s.shutdown(socket.SHUT_WR)
print("File berhasil dikirim!")
print(s.recv(1024).decode())
s.close()
