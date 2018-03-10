import socket # mengimport library socket

UDP_IP = "127.0.0.1" # menassign variabel UDP_IP yang diinginkan
UDP_PORT = 5005 # menassign variabel UDP_PORT yang diinginkan
PESAN = "Hello World!" # menassign variabel PESAN dengan pesan yang diinginkan

print ("target IP:", UDP_IP) # menampilkan target IP 
print ("target port:", UDP_PORT) # menampilkan target port
print ("pesan:", PESAN) # menampilkan pesan

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(PESAN.encode(), (UDP_IP, UDP_PORT)) # mengirim data melalui socket yang telah dibuat