import socket # mengimport library socket

UDP_IP = "127.0.0.1" # menassign variabel UDP_IP yang diinginkan
UDP_PORT = 5005 # menassign variabel UDP_PORT yang diinginkan

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT)) # memasukkan UDP_IP dan UDP_PORT ke dalam socket

while True:
    data, addr = sock.recvfrom(1024) # menerima data dari client
    print (addr) # menampilakn alamat IP client
    print ("pesan diterima:", data.decode()) # menampilkan pesan yang diterima dari client
