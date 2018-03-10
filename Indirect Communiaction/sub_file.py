import zmq

context = zmq.Context()


sock = context.socket(zmq.SUB)


sock.setsockopt(zmq.SUBSCRIBE, b"1")
sock.connect("tcp://127.0.0.1:5680")

while True:
    file = sock.recv()
    
    with open("uploaded file.pptx", "wb") as handle:
        handle.write(file)
        handle.close()