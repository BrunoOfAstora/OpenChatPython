import requests
import socket

def main():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip = response.json()['ip']
        return ip
    except requests.exceptions.RequestException as e:
        return f"Falha ao obter o IP: {e}"

def socketMain():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 8080

    server.bind((server_ip, port))

    server.listen(0)
    print("Ouvindo " + server_ip + " na porta " + str(port))

    client_socket, client_address = server.accept()
    print(f"Conexão de " + {client_address} + ":" + {client_socket} + " aceita." )

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break
    print(f"Recebido: " + {request})

    response = "Accepted".encode("utf-8")
    client_socket.send(response)

    client_socket.close()
    print("Conexão fechada")
    server.close()
    print(f"Servidor fechado")

if __name__ == "__main__":
    ip = main()
    print(f"IPv4: {ip}")
    socketMain()
