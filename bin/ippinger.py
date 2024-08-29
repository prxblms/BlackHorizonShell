import subprocess, platform

def IPPinger(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    try:
        result = subprocess.run(['ping', param, '1', ip], capture_output = True, text = True, check = True)
        print(result.stdout)
    except subprocess.CalledProcessError as error:
        print(f" Erro: {error}")

def main():
    ip = input(" > ")
    IPPinger(ip)

if __name__ == '__main__':
    main()