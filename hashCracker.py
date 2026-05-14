import hashlib
import sys
from colorama import Style, Fore
x = sys.argv[1]
with open ("subdomain.txt","r") as file:
    y = file.read()
z = y.splitlines()
for i in z :
    b = i.encode()
    v = hashlib.md5(b).hexdigest()
    if v == x : 
        print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+i)