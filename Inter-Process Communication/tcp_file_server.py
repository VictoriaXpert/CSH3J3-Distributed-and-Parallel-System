import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

f = open("hasil.txt", "wb")
while True:
    conn, addr = s.accept()
    print("Terhubung dengan", addr)
    print("Sedang menerima file... ")
    data = conn.recv(1024)
    while (data):
        f.write(data)
        data = conn.recv(1024)
    f.close()
    print("File berhasil diterima!")
    conn.send("Terima kasih telah terkoneksi".encode())
    conn.close()
