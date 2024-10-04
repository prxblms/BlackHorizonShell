import os
from colorama import Fore as fg

user = os.getlogin() # get local username of computer.
cwd = os.getcwd() # get absolut path of tool.

# Here I transformed INPUT into a function to optimize the code, as I will use INPUT several times. 
def get_input():
    print(f"\n {fg.RED}┌─ͼ[ {fg.LIGHTWHITE_EX}{user} {fg.RED}>> BlackHorizon ]ͽ ")
    command = input(f" └───ͼ Enter the command: {fg.LIGHTWHITE_EX}")
    return command

def list_ip_pingers():
    path = f'{cwd}\\bin\\ippingers'
    count = 0
    list = []

    for pinger in os.listdir(path):
        if pinger.endswith(('.py', '.bat', '.exe')):
            if pinger in list:
               break
            else:
                list.append(pinger)

    print(list)