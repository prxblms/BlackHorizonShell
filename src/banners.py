from colorama import Fore as fg

def BH_CMDS_BANNER():
    return(f'''
    {fg.RED}[ {fg.LIGHTWHITE_EX}ip pinger {fg.RED}] {fg.LIGHTRED_EX}
    {fg.RED}[ {fg.LIGHTWHITE_EX}ip lookup {fg.RED}] {fg.LIGHTRED_EX}''')

def DEFAULT_CMDS_BANNER():
    return(f'''
    {fg.RED}[ {fg.LIGHTWHITE_EX}help  {fg.RED}] {fg.LIGHTRED_EX}
    {fg.RED}[ {fg.LIGHTWHITE_EX}exit  {fg.RED}] {fg.LIGHTRED_EX}
    {fg.RED}[ {fg.LIGHTWHITE_EX}clear {fg.RED}] {fg.LIGHTRED_EX}''')

def HELP_BANNER():
    return(f'''
    {fg.RED}[ {fg.LIGHTWHITE_EX}cmds    {fg.RED}] {fg.LIGHTRED_EX}show default commands (exit, clean and more...)
    {fg.RED}[ {fg.LIGHTWHITE_EX}bh cmds {fg.RED}] {fg.LIGHTRED_EX}show special commands provided by Black Horizon.''')

def BH_BANNER():
    return(f'''{fg.RED}
                      ╔╗ ╦  ╔═╗╔═╗╦╔═  ╦ ╦╔═╗╦═╗╦╔═╗╔═╗╔╗╔
                      ╠╩╗║  ╠═╣║  ╠╩╗  ╠═╣║ ║╠╦╝║╔═╝║ ║║║║
                      ╚═╝╩═╝╩ ╩╚═╝╩ ╩  ╩ ╩╚═╝╩╚═╩╚═╝╚═╝╝╚╝
                   {fg.LIGHTRED_EX}Developed by {fg.LIGHTWHITE_EX}@27prxblms {fg.LIGHTRED_EX}- version 1.0 BETA''')