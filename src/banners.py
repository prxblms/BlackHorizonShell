import os
from colorama import Fore as fg

def BH_CMDS_BANNER():
    return(f'''
    {fg.RED}[ {fg.LIGHTRED_EX}ip pinger {fg.RED}] {fg.WHITE}
    {fg.RED}[ {fg.LIGHTRED_EX}ip lookup {fg.RED}] {fg.WHITE}''')

def DEFAULT_CMDS_BANNER():
    return(f'''
    {fg.RED}[ {fg.LIGHTRED_EX}help  {fg.RED}] {fg.LIGHTRED_EX}
    {fg.RED}[ {fg.LIGHTRED_EX}exit  {fg.RED}] {fg.LIGHTRED_EX}
    {fg.RED}[ {fg.LIGHTRED_EX}clear {fg.RED}] {fg.LIGHTRED_EX}''')

def HELP_BANNER():
    return(f'''
    {fg.RED}[ {fg.LIGHTRED_EX}cmds    {fg.RED}] {fg.LIGHTWHITE_EX}show default commands (exit, clean and more...)
    {fg.RED}[ {fg.LIGHTRED_EX}bh cmds {fg.RED}] {fg.LIGHTWHITE_EX}show special commands provided by Black Horizon.''')

def BH_BANNER():
    return(f'''{fg.RED}
                      ╔╗ ╦  ╔═╗╔═╗╦╔═  ╦ ╦╔═╗╦═╗╦╔═╗╔═╗╔╗╔
                      ╠╩╗║  ╠═╣║  ╠╩╗  ╠═╣║ ║╠╦╝║╔═╝║ ║║║║
                      ╚═╝╩═╝╩ ╩╚═╝╩ ╩  ╩ ╩╚═╝╩╚═╩╚═╝╚═╝╝╚╝
                   {fg.LIGHTWHITE_EX}Developed by {fg.RED}@27prxblms {fg.LIGHTWHITE_EX}- version 1.0 BETA''')