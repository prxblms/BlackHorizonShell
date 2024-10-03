import os
import sys
import time
import socket
from colorama import Fore as fg

def banner():
    return(f'''{fg.RED}
               ┏┓━┓      ┓ ┓      ┳┏┓  ┏┓          •      ┏┓┓    ┓ 
               ┏┛ ┃┏┓┏┓┓┏┣┓┃┏┳┓┏  ┃┃┃  ┃ ┏┓┏┓┏┓┏┓┏╋┓┏┓┏┓  ┃ ┣┓┏┓┏┃┏
               ┗━ ╹┣┛┛ ┛┗┗┛┗┛┗┗┛  ┻┣┛  ┗┛┗┛┛┗┛┗┗ ┗┗┗┗┛┛┗  ┗┛┛┗┗ ┗┛┗
                   ┛                                               
               {fg.LIGHTWHITE_EX}Developed by {fg.LIGHTGREEN_EX}27prxblms {fg.LIGHTWHITE_EX}- https://github.com/prxblms''')

class IPPinger:
    def __init__(self):
        self.user = os.getlogin()
        os.system('title 27prxblms IP Connection Check')
        print(banner())

        self.get_ip()
        self.get_port()
        self.pinging(self.ip, self.port)

    # here check if the user entered a valid IP.
    def get_ip(self):
        while True:
            print(f"\n {fg.RED}┌─[{fg.LIGHTWHITE_EX}user: {fg.LIGHTRED_EX}{self.user}{fg.RED}]")
            ip = input(f" │\n {fg.RED}├───ͼމ {fg.LIGHTWHITE_EX}enter the IP: {fg.LIGHTGREEN_EX}")
            if not ip:
                print(f"\n {fg.LIGHTRED_EX}27prxblms: {fg.LIGHTWHITE_EX}{self.user} you need to type something, preferably a valid IP.")

            else:
                try:
                    socket.inet_pton(socket.AF_INET, ip)
                    self.ip = ip
                    break
                
                except socket.error:
                    pass

                try:
                    socket.inet_pton(socket.AF_INET6, ip)
                    self.ip = ip
                    break
                
                except socket.error:
                    pass

                print(f"\n {fg.LIGHTRED_EX}27prxblms: {fg.LIGHTWHITE_EX}{self.user} you entered something that is not recognized as a valid IP.")
                print(f"\n {fg.LIGHTRED_EX}27prxblms: {fg.LIGHTWHITE_EX}{self.user} try again.")

    # here check if the user entered a valid Port.
    def get_port(self):
        while True:
            port = input(f" │\n {fg.RED}└───ͼމ {fg.LIGHTWHITE_EX}enter the Port: {fg.LIGHTGREEN_EX}")

            if not port:
                print(" you dont enter a valid Port.")

            elif not port.isdigit():
                print(" please insert a Port, not a text, idiot.")

            else:
                self.port = port
                break

    # here check the connection with IP and Port.
    def pinging(self, ip, port):
        timeout = 5

        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(timeout)

                    # Try connecting to IP and port.
                    s.connect((ip, int(port)))
                    print(f"CONNECTED {ip} AND PORT {port} SUCESSFULLY!")
                    time.sleep(3)

            except (socket.timeout, socket.error):
                print(f" IP: {ip} OFFLINE OR {port} CLOSED...")
                time.sleep(3)

if __name__ == '__main__':
    try:
        IPPinger()
    except KeyboardInterrupt:
        print(" Finishing! ")
        sys.exit(0)