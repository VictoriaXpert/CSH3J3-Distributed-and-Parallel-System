import zmq  # mengimport modul zero MQ
import time  # mengimport library time

context = zmq.Context() # membuat context zmq baru

sock = context.socket(zmq.PUSH)  # menentukan tipe soket PUSH
sock.bind("tcp://10.20.0.252:5680") # menentukan protokol, IP address, dan port

id = 0 # menginisialisasi id pesan bernilai 0

while True: # berjalan selama kondisi true
    time.sleep(1) # memberi jeda selama 1 detik
    id, now = id+1, time.ctime()
    message = "{id} - {time}".format(id=id, time=now)
    sock.send(message.encode())
    print ("Sent: {msg}".format(msg=message))