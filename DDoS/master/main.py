"""
message_format = {
    "type": "attack", # "attack" or "stop"
    "target_ip": "0.0.0.0",
    "attack_type": "icmp",
    "number_of_attack": -1 # -1 for unlimited attack
}
"""

import xmlrpc.client


botnet_list = []


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


if __name__ == '__main__':
    pass
