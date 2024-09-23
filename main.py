import os, sys
from src.functions import *
from src.commands import *

def HelpMenu():
    DelayPrint(f"""
    - help       - clear
    - exit xampp - clear temp files
    """)

class main:
    def __init__(self):
        # os.chdir('C:\Xzhyan')
        os.system('cls && title Black Horizon')
        Banner() # Logo ASCII da ferramenta.

        self.command_list = [
            'exit', 'help', 'clear', 'ls',
            'clear temp files', 'ip pinger',
            'py', 'python'
            ]

        self.run()

    def run(self):
        while True:
            try:
                current_dir = os.getcwd() # Diretorio atual.
                print(f'\n {current_dir}')
                cmd = input(f" {fg.RED}BlackHorizon~$ {fg.WHITE}")
                args = cmd.split()

                if cmd in self.command_list:
                    
                    if cmd == 'clear':
                        os.system('cls')

                    elif cmd == 'help':
                        print(f'\n{self.command_list}')
                    
                    elif cmd == 'exit':
                        sys.exit()
                    
                    elif cmd == 'ls':
                        os.system('dir /b')

                    elif cmd == 'clear temp files':
                        print('')
                        DeleteTempFiles()

                    elif cmd == 'ip pinger':
                        print(pinger_list)

                    else:
                        os.system(cmd)

                elif len(args) == 2:
                    cmd = args[0]
                    arg = args[1]

                    if cmd == 'py' or cmd == 'python':
                        os.system(f'{cmd} {arg}')

                    elif cmd == 'cd':
                        try:
                            os.chdir(arg)
                        except:
                            DelayPrint("\n - you need to enter a directory.\n - example: cd DirectoryName.\n")

                    elif cmd == 'pinger':
                        IPPingers(arg)

                else:
                    DelayPrint(f"\n   '{cmd}' this command does not exist \n")

            except KeyboardInterrupt: # Fecha a ferramenta quando Ctrl-C for precionado.
                DelayPrint(f"\n\n  Ctrl-C was pressed, type {fg.RED}exit {fg.WHITE}to exit the tool.\n ")
                #sys.exit()
            except Exception as error:
                DelayPrint(f"an unexpected error occurred: {error}")

if __name__ == '__main__':
    main()
