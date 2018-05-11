# DDoS Attack Program with ICMP and SYN Flooding Attack

## How to Run
### For Both
1. turn off the firewall

### For Master
1. run ip_registrar.py file first
2. run main_master.py file
3. Use the menu properly

### For BotNet/Zombie/Slave
1. install scapy module (pip install scapy)
2. edit main_botnet.py file
3. change ip_master=<master_ip_address> in line 94
4. run main_botnet.py file
5. Now, you're listen to master