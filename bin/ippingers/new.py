import socket
import time

def verificar_ip(ip, porta=80, timeout=5):
    try:
        # Cria um socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            # Tenta conectar ao IP na porta especificada
            s.connect((ip, porta))
            print(f'O IP {ip} está online na porta {porta}.')
    except (socket.timeout, socket.error):
        print(f'O IP {ip} está offline ou a porta {porta} está fechada.')

if __name__ == '__main__':
    ip_para_verificar = input("Digite o IP para verificar: ")
    porta_para_verificar = int(input("Digite a porta (padrão 80): ") or 80)
    
    while True:
        verificar_ip(ip_para_verificar, porta_para_verificar)
        time.sleep(5)  # Espera 5 segundos antes de verificar novamente
