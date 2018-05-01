"""
message_format = {
    "type": "attack", # "attack" or "stop"
    "target_ip": "0.0.0.0",
    "attack_type": "icmp",
    "number_of_attack": -1 # -1 for unlimited attack
}
"""

import xmlrpc.client
import os


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
    ip_list = []
    with open("botnet_list.txt", "r") as file:
        ip_list = file.readlines()
        ip_list = [x.strip() for x in ip_list]
    return ip_list


def parseMenu(menu):
    if menu == "1":
        pass
    elif menu == "2":
        botnet_list = viewBotnet()
        print("*** BotNet List ***")
        print(botnet_list)

botnet_list = []
if __name__ == '__main__':
    botnet_list = []
    menu = 0
    while menu != 99:
        print("========== Welcome to DDoS Attack Application! ==========")
        parseMenu(menu)        
        print("1. Attack Target")
        print("2. View Botnet List")
        print("Select: ", end="")
        menu = str(input())
        os.system("cls")
        