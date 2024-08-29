import os, sys

from src.funcs import *
from src.cmds import *

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
            'clear',
            'echo',
            'ping',
            'exit',
            'composer',
            'npm',
            'mkdir',
            'clear temp files'
            ]

        self.run()

    def run(self):
        while True:
            try:
                current_dir = os.getcwd() # Diretorio atual.
                print(f'\n {current_dir}')
                cmd = input(f" {fg.RED}BlackHorizon~$ {fg.WHITE}")
                full_cmd = cmd # comando sem a separação em args.
                args = cmd.split()

                if len(args) == 2:
                    cmd = args[0]
                    arg = args[1]

                if cmd == 'py' or cmd == 'python':
                    os.system(f"{cmd} {arg}")

                if cmd == 'help':
                    HelpMenu()
                
                elif cmd == 'exit':
                    sys.exit()

                elif cmd == 'clear':
                    os.system('cls')
                
                elif cmd == 'ls':
                    os.system('dir /b')

                elif cmd == 'clear temp files':
                    print('')
                    DeleteTempFiles()

                elif cmd == 'cd':
                    try:
                        os.chdir(arg)
                    except:
                        DelayPrint("\n - you need to enter a directory.\n - example: cd DirectoryName.\n")

                # executa comandos completos.
                elif cmd in self.command_list:
                    os.system(full_cmd)
                else:
                    DelayPrint(f"\n   '{full_cmd}' this command does not exist \n")


            except KeyboardInterrupt: # Fecha a ferramenta quando Ctrl-C for precionado.
                DelayPrint(f"\n\n  Ctrl-C was pressed, type {fg.RED}exit {fg.WHITE}to exit the tool.\n ")
                #sys.exit()
            except Exception as error:
                DelayPrint(f"an unexpected error occurred: {error}")

if __name__ == '__main__':
    main()
