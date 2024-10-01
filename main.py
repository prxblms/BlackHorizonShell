import os
import sys
from src.commands import DEFAULT_COMMANDS, BH_COMMANDS
from src.banners import BH_BANNER, HELP_BANNER, BH_CMDS_BANNER, DEFAULT_CMDS_BANNER
from src.functions import get_input
from colorama import Fore as fg

class BlackHorizon:
    def __init__(self):
        print(BH_BANNER())
        self.command_line()

    # Special commands function.
    def bh_command(self, command):
        if command == 'ip lookup':
            os.system('start python bin/iplookup/iplookup.py')

        elif command == 'ip pinger':
            os.system('start python bin/ippingers/prxblms.py')

    # Default commands function.
    def default_command(self, command):
        if command == 'help':
            print(HELP_BANNER())
        
        elif command == 'exit':
            print("\n finishing...")
            sys.exit(0)

        elif command == 'clear':
            os.system('cls')

        elif command == 'cmds':
            print(DEFAULT_CMDS_BANNER())

        elif command == 'bh cmds':
            print(BH_CMDS_BANNER())




    # The main loop of the tool.
    # Here valid commands are checked and directed to their respective functions.
    def command_line(self):
        while True:
            command = get_input()

            if not command:
                print(f"\n {fg.LIGHTWHITE_EX}please enter a valid command!")
                continue

            elif command in DEFAULT_COMMANDS:
                self.default_command(command)

            elif command in BH_COMMANDS:
                self.bh_command(command)

            else:
                print(f"\n {fg.RED}[ {fg.LIGHTRED_EX}{command} {fg.RED}] {fg.LIGHTWHITE_EX}this command was not found! ")



if __name__ == '__main__':
    try:
        BlackHorizon()
    except KeyboardInterrupt:
        print("\n finishing...")
        sys.exit(0)