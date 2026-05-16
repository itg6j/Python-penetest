import socket
from colorama import Fore,Style
ip = "142.251.39.174"
ports = range(80,100)
open_list=[]
def check (ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    r = sock.connect_ex((ip,port))
    if r == 0 : 
        sock.close()
    return r
for port in ports : 
    response = check (ip,port)
    if response == 0 :
        open_list.append(port)
print(Fore.BLUE+"[+] "+Style.RESET_ALL+"port open is : ",open_list)