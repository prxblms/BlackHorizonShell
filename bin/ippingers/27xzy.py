import os, sys, time, socket

class IPPinger:
    def __init__(self):
        self.get_input()

    def get_input(self):
        ip = input(" enter the IP or Host: ")
        if not ip:
            print(" you dont enter a valid IP.")
            self.get_input()
        else:
            self.pinging(ip)

    def pinging(self, ip):
        while True:
            try:
                pinging = os.system(f'PING - 1 {ip} >nul')
                
                if pinging == 1:
                    print("testing connection")
                
                else:
                    print(" erro")

            except Exception as e:
                print(e)

if __name__ == '__main__':
    try:
        IPPinger()
    except KeyboardInterrupt:
        print(" Finishing! ")
        sys.exit(0)