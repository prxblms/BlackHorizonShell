import os
from colorama import Fore as fg

user = os.getlogin()

def get_input():
    print(f"\n {fg.RED}┌─ͼ[ {fg.LIGHTWHITE_EX}{user} {fg.RED}>> BlackHorizon ]ͽ ")
    command = input(f" └───ͼ Enter the command: {fg.LIGHTWHITE_EX}")
    return command