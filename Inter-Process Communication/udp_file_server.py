import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

f = open("hasil.txt", "wb")
while True:
    data, addr = s.recvfrom(1024)
    print("Terhubung dengan", addr)
    print("Sedang menerima file... ")
    # data = data.recv(1024)
    while (data):
        f.write(data)
        data = s.recv(1024)
        if not data:
            break
    f.close()
    print("File berhasil diterima!")
