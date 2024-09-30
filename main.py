import os
import sys
from src.commands import DEFAULT_COMMANDS, BH_COMMANDS
from src.banners import BH_BANNER
from src.functions import get_input

class BlackHorizon:
    def __init__(self):
        print(BH_BANNER())
        self.command_line()

    def bh_command(self, command):
        if command == 'ip lookup':
            print(" IP Lookup")

    def default_command(self, command):
        if command == 'help':
            print(" Help")
        
        elif command == 'exit':
            print("\n finishing...")
            sys.exit(0)

        elif command == 'clear':
            os.system('cls')

    def command_line(self):
        while True:
            command = get_input()

            if not command:
                print("\n please enter a valid command!")
                continue

            elif command in DEFAULT_COMMANDS:
                self.default_command(command)

            elif command in BH_COMMANDS:
                self.bh_command(command)

            else:
                print(f"\n [ {command} ] this command was not found! ")

if __name__ == '__main__':
    try:
        BlackHorizon()
    except KeyboardInterrupt:
        print("\n finishing...")
        sys.exit(0)