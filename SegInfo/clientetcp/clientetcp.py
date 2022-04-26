import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso")

    HostAlvo = input("Digite Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente conectado com Sucesso: " + HostAlvo + " e na Porta:" + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no host: " + HostAlvo + " e na Porta:" + PortaAlvo)
        print("Erro: {}".format(e))
        sys.exit()


if __name__ == "__main__":
    main()