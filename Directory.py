import requests
import sys
from colorama import Style,Fore
with open("subdomain.txt" ,"r")as file :
    directories= file.read()
dirList = directories.splitlines()
for i in dirList :
    dir = f"https://{sys.argv[1]}/{i}"
    try :
        re = requests.get(dir)
        if re.status_code == 200 : 
            print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+dir)
    except requests.ConnectionError : 
        pass

