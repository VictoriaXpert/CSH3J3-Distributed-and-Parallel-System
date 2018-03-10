import socket # mengimport library socket

TCP_IP = '192.168.43.135'  # menassign variabel TCP_IP dengan IP server
TCP_PORT = 5005 # menassign variabel TCP_PORT dengan port yang diinginkan
BUFFER_SIZE = 1024  # menassign variabel BUFFER_SIZE dengan ukuran buffer yang diinginkan

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # menentukan family socket dan type dari TCP
s.bind((TCP_IP, TCP_PORT)) # untuk melakukan binding, input harus berupa tuple (IP, PORT)
s.listen(1) # merubah kondisi socket menjadi siap menerima koneksi

while 1:
    conn, addr = s.accept() # mendapkatkan socket dari klien
    print ('Alamat koneksi:', addr) # menampilkan alamat IP dari koneksi yang terbuat
    data = conn.recv(BUFFER_SIZE) # menerima data dari socket
    print ("Pesan diterima:", data.decode()) # menampilkan pesan yang diterima
    conn.send(data) # mengirim pesan BUFFER_SIZE
conn.close() # untuk menutup socket
