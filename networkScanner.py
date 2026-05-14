from scapy.all import *
interface = "wlan0"
ipaddress = "10.99.x.x/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"
packet = Ether(dst= broadcastMac)/ARP(pdst = ipaddress)
ans, unans = srp(packet,timeout = 2 , iface = interface, inter = 0.1)
for sender , resiver in ans : 
    print(resiver.sprintf(r"%Ether.src% - %ARP.psrc%"))