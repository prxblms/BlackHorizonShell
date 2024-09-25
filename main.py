import os, sys
from src.banners import *
from src.functions import *
from src.commands import *

_lang_ = translator()

class Main:
    def __init__(self):
        # os.chdir('C:\Xzhyan')
        os.system('cls && title Black Horizon')
        banner() # ASCII logo of the tool.

        self.run()

    def run(self):
        while True:
            try:
                current_dir = os.getcwd() # current dir.
                last_dir = os.path.basename(current_dir)
                print(f'\n {fg.WHITE}dir: \{fg.LIGHTRED_EX}{last_dir}')
                cmd = input(f" {fg.RED}BlackHorizon~$ {fg.WHITE}")
                print('')
                args = cmd.split()

                if cmd in command_list:
                    
                    if cmd == 'clear':
                        os.system('cls')

                    elif cmd == 'exit':
                        sys.exit()

                    elif cmd == 'help':
                        helpMenu()

                    elif cmd == 'commands':
                        normalCommads()
                    
                    elif cmd == 'ls':
                        os.system('dir /b')

                    elif cmd == 'clear temp files':
                        deleteTempFiles()

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
                            delayPrint(f'\n - {_lang_("you need to enter a directory.")}\n - {_lang_("example: cd DirectoryName.")}\n')

                    elif cmd == 'pinger':
                        ipPingers(arg)

                    elif cmd == 'setlang':
                        setLanguage(arg)

                else:
                    delayPrint(f'\n   [ {cmd} ] {_lang_("this command does not exist")} \n')

            except KeyboardInterrupt: # close tool when Ctrl-C is pressed.
                delayPrint(f'\n\n  {_lang_("Ctrl-C was pressed, type")} {fg.RED}exit {fg.WHITE}{_lang_("to exit the tool.")}\n ')
                #sys.exit()
            except Exception as error:
                delayPrint(f'{_lang_("an unexpected error occurred:")} {error}')

if __name__ == '__main__':
    Main()
