import os, sys
from colorama import Fore

def Banner():
    print(f"""
        {Fore.RED} ██▓███  {Fore.WHITE} ██▀███  {Fore.RED}▒██   ██▒{Fore.WHITE} ▄▄▄▄   {Fore.RED} ██▓    {Fore.WHITE} ███▄ ▄███▓{Fore.RED}  ██████ 
        {Fore.RED}▓██░  ██▒{Fore.WHITE}▓██ ▒ ██▒{Fore.RED}▒▒ █ █ ▒░{Fore.WHITE}▓█████▄ {Fore.RED}▓██▒    {Fore.WHITE}▓██▒▀█▀ ██▒{Fore.RED}▒██    ▒ 
        {Fore.RED}▓██░ ██▓▒{Fore.WHITE}▓██ ░▄█ ▒{Fore.RED}░░  █   ░{Fore.WHITE}▒██▒ ▄██{Fore.RED}▒██░    {Fore.WHITE}▓██    ▓██░{Fore.RED}░ ▓██▄   
        {Fore.RED}▒██▄█▓▒ ▒{Fore.WHITE}▒██▀▀█▄  {Fore.RED} ░ █ █ ▒ {Fore.WHITE}▒██░█▀  {Fore.RED}▒██░    {Fore.WHITE}▒██    ▒██ {Fore.RED}  ▒   ██▒
        {Fore.RED}▒██▒ ░  ░{Fore.WHITE}░██▓ ▒██▒{Fore.RED}▒██▒ ▒██▒{Fore.WHITE}░▓█  ▀█▓{Fore.RED}░██████▒{Fore.WHITE}▒██▒   ░██▒{Fore.RED}▒██████▒▒
        {Fore.RED}▒▓▒░ ░  ░{Fore.WHITE}░ ▒▓ ░▒▓░{Fore.RED}▒▒ ░ ░▓ ░{Fore.WHITE}░▒▓███▀▒{Fore.RED}░ ▒░▓  ░{Fore.WHITE}░ ▒░   ░  ░{Fore.RED}▒ ▒▓▒ ▒ ░
        {Fore.RED}░▒ ░     {Fore.WHITE}  ░▒ ░ ▒░{Fore.RED}░░   ░▒ ░{Fore.WHITE}▒░▒   ░ {Fore.RED}░ ░ ▒  ░{Fore.WHITE}░  ░      ░{Fore.RED}░ ░▒  ░ ░
        {Fore.RED}░░       {Fore.WHITE}  ░░   ░ {Fore.RED} ░    ░  {Fore.WHITE} ░    ░ {Fore.RED}  ░ ░   {Fore.WHITE}░      ░   {Fore.RED}░  ░  ░  
        {Fore.RED}         {Fore.WHITE}   ░     {Fore.RED} ░    ░  {Fore.WHITE} ░      {Fore.RED}    ░  ░{Fore.WHITE}       ░   {Fore.RED}      ░  
""")

def main():
    os.system("cls && title ᴘʀxʙʟᴍs ~ ɪᴘ ᴘɪɴɢᴇʀ")
    Banner()
    ip = input(f"   {Fore.RED}Enter the {Fore.LIGHTWHITE_EX}IP {Fore.RED}or {Fore.LIGHTWHITE_EX}{Fore.RED}Host: {Fore.LIGHTGREEN_EX}")
    print("")
    while True:
        try:
            pinging = os.system(f'PING -n 1 {ip} >nul')
            if ip == '':
                main()
            elif pinging == 0:
                print(f" {Fore.LIGHTGREEN_EX}Testing Connection to {Fore.LIGHTWHITE_EX}IP{Fore.LIGHTWHITE_EX}/{Fore.LIGHTWHITE_EX}Host: {Fore.LIGHTGREEN_EX}{ip} {Fore.LIGHTWHITE_EX}>>> {Fore.LIGHTGREEN_EX}Connected Successfully{Fore.LIGHTWHITE_EX}!!!")
            else:
                print(f" {Fore.RED}IP{Fore.LIGHTWHITE_EX}/{Fore.RED}Host: {Fore.RED}{ip} {Fore.LIGHTWHITE_EX}>>> {Fore.RED}Offline connection{Fore.LIGHTWHITE_EX}!")

        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()