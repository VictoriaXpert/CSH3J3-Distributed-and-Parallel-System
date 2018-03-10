import socket # mengimport library socket

TCP_IP = '192.168.43.135' # menassign variabel TCP_IP yang diinginkan
TCP_PORT = 5005 # menassign variabel TCP_PORT yang diinginkan
BUFFER_SIZE = 1024  # menassign variabel BUFFER_SIZE dengan ukuran buffer yang diinginkan
PESAN = "Hello World!" # menassign variabel PESAN dengan pesan yang diinginkan

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # menentukan family socket dan type dari TCP
s.connect((TCP_IP, TCP_PORT)) # client meminta koneksi kepada server
s.send(PESAN.encode()) # mengirim pesan ke server
data = s.recv(BUFFER_SIZE) # menerima data dari socket
s.close() # menutup soket

print ("pesan diterima:", data.decode()) # menampilan pesan dari server