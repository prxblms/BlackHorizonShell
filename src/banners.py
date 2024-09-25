from colorama import Fore as fg
from src.functions import translator

_lang_ = translator()

command_list = [
    'clear',
    'exit',
    'help',
    'commands',
    'ls',
    'clear temp files',
    'ip pinger'
]

def normalCommads():
    print(f"""
    {fg.WHITE}[ {fg.LIGHTRED_EX}clear {fg.WHITE}] - {_lang_('clean the tool screen')}
    {fg.WHITE}[ {fg.LIGHTRED_EX}exit {fg.WHITE}] - {_lang_('close the tool')}
    {fg.WHITE}[ {fg.LIGHTRED_EX}ls {fg.WHITE}] - {_lang_('show directory files and folders')}
    """)

def helpMenu():
    print(f"""
    {fg.WHITE}[ {fg.LIGHTRED_EX}commands {fg.WHITE}] - {_lang_('show normal commands to use')}
    {fg.WHITE}[ {fg.LIGHTRED_EX}bh cmds  {fg.WHITE}] - {_lang_('show Black Horizon special commands to use')}
    """)

def banner():
    print(f'''{fg.RED}
                        ╔╗ ╦  ╔═╗╔═╗╦╔═  ╦ ╦╔═╗╦═╗╦╔═╗╔═╗╔╗╔
                        ╠╩╗║  ╠═╣║  ╠╩╗  ╠═╣║ ║╠╦╝║╔═╝║ ║║║║
                        ╚═╝╩═╝╩ ╩╚═╝╩ ╩  ╩ ╩╚═╝╩╚═╩╚═╝╚═╝╝╚╝
                               {fg.WHITE}Developed by {fg.LIGHTRED_EX}27prxblms

    {fg.WHITE}{_lang_("type")} [ {fg.LIGHTRED_EX}help {fg.WHITE}] {_lang_("to display the help menu")}''')