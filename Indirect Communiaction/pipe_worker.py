import zmq

context = zmq.Context()


sock = context.socket(zmq.PULL)
sock.connect("tcp://10.20.0.252:5680")

while True:
    message = sock.recv()
    print ("Received: {msg}".format(msg=message))