import ipaddress
from subprocess import Popen
import colorama
from colorama import Fore
server = ipaddress.ip_network('192.168.21.208')
for x in server.hosts():
    x = str(x)
    hostup = Popen(["ping", "-c1", x])
    output = hostup.communicate()[0]
    val1 = hostup.returncode
    if val1 == 0:
        print(Fore.GREEN+ x, "UP server is pinging")
    else:
        print(Fore.RED+ x, "DOWN server is not responding")

