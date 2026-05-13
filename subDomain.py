import sys
import requests
from colorama import Fore,Style
sub_list = open("subdomain.txt").read()
subdomain = sub_list.splitlines()
for sub in subdomain :
        sub_domain = f"http://{sub}.{sys.argv[1]}"
        try : 
            x = requests.get(sub_domain)
            if x.status_code == 200 :
                    print(Fore.BLUE+"[+] "+Style.RESET_ALL+Style.BRIGHT+sub_domain)
        except requests.ConnectionError:
               pass