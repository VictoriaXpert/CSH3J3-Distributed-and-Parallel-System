import time # mengimport library time
import zmq # mengimport module zero mq

context = zmq.Context() # membuat variabel baru dari zmq Context
socket = context.socket(zmq.REP) # membuat socket baru dengan tipe REPLY
socket.bind("tcp://10.20.0.252:5555") # menginput protokol, IP address, dan port

while True: # Berjalan selama kondisi True
    message = socket.recv() # socket/server menerima pesan yang dikirim
    print("Received request: %s" % message) # memunculkan pesan yang diterima

    # do some work
    time.sleep(1) # membuat delay 1 detik

    socket.send(b"World") # mengirim pesan kepada client
