import time
from colorama import Fore as fg

# def DelayPrint2(text):
#     for x in text:
#         sys.stdout.write(x)
#         sys.stdout.flush()
#         time.sleep(0.02)

def DelayPrint(text):
    for x in text:
        time.sleep(0.02)
        print(x, end='', flush=True)

def Banner():
    print(f"""{fg.RED}
                        ╔╗ ╦  ╔═╗╔═╗╦╔═  ╦ ╦╔═╗╦═╗╦╔═╗╔═╗╔╗╔
                        ╠╩╗║  ╠═╣║  ╠╩╗  ╠═╣║ ║╠╦╝║╔═╝║ ║║║║
                        ╚═╝╩═╝╩ ╩╚═╝╩ ╩  ╩ ╩╚═╝╩╚═╩╚═╝╚═╝╝╚╝
                               Developed by {fg.WHITE}27prxblms""")