import zmq # mengimport modul zero MQ
import time # mengimport library time

context = zmq.Context() # membuat context zmq baru

sock = context.socket(zmq.PUB) # menentukan tipe soket PUB
sock.bind("tcp://10.20.0.252:5680") # menentukan protokol, IP address, dan port

id = 0 # menginisialisasi id pesan bernilai 0

while True: # berjalan selama kondisi true
    time.sleep(1) # memberi jeda selama 1 detik
    id, now = id+1, time.ctime() # id pesan ditambah 1 dan membuat variabel now menjadi waktu di laptop/pc

    message = "1-Update! >> #{id} >> {time}".format(id=id, time=now) # mengassign variabel message dengan pesan yang diinginkan
    sock.send(message.encode('ascii')) # mengirim pesan jika klien memilih pesan dengan id 1

    message = "2-Update! >> #{id} >> {time}".format(id=id, time=now)  # mengassign variabel message dengan pesan yang diinginkan
    sock.send(message.encode('ascii')) # mengirim pesan jika klien memilih pesan dengan id 1

    id += 1 # id ditambah dengan 1