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
            'clear',
            'echo',
            'ping',
            'exit',
            'composer',
            'npm',
            'mkdir',
            'clear temp files',
            'ip pinger'
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

                if cmd in self.command_list:
                    
                    if cmd == 'clear':
                        os.system('cls')
    
                    elif len(args) == 2:
                        cmd = args[0]
                        arg = args[1]

                        if cmd == 'py' or cmd == 'python':
                            os.system(f'{cmd} {arg}')

                    else:
                        os.system(full_cmd)

                else:
                    DelayPrint(f"\n   '{full_cmd}' this command does not exist \n")

                # if cmd == 'help':
                #     print(self.command_list)
                
                # if cmd == 'exit':
                #     sys.exit()

                # if cmd == 'clear':
                #     os.system('cls')
                
                # if cmd == 'ls':
                #     os.system('dir /b')

                # if cmd == 'clear temp files':
                #     print('')
                #     DeleteTempFiles()

                # if cmd == 'ip pinger':
                #     print(pinger_list)

                # if len(args) == 2:
                #     cmd = args[0]
                #     arg = args[1]

                #     if cmd == 'cd':
                #         try:
                #             os.chdir(arg)
                #         except:
                #             DelayPrint("\n - you need to enter a directory.\n - example: cd DirectoryName.\n")

                #     elif cmd == 'pinger':
                #         IPPingers(arg)

                # # executa comandos completos.
                # elif cmd in self.command_list:
                #     os.system(full_cmd)
                # else:
                #     DelayPrint(f"\n   '{full_cmd}' this command does not exist \n")

            except KeyboardInterrupt: # Fecha a ferramenta quando Ctrl-C for precionado.
                DelayPrint(f"\n\n  Ctrl-C was pressed, type {fg.RED}exit {fg.WHITE}to exit the tool.\n ")
                #sys.exit()
            except Exception as error:
                DelayPrint(f"an unexpected error occurred: {error}")

if __name__ == '__main__':
    main()
