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

    server_ip = input("Enter IP Address: ")
    port = int(input("Enter Port: "))

    try:
        server.bind((server_ip, port))
    except OSError as e:
        print(f"Erro ao vincular {server_ip}:{port} -> {e}")
        exit()

    server.listen(1)
    print(f"Ouvindo {server_ip} na porta {port}")

    client_socket, client_address = server.accept()
    print(f"Conexão de {client_address} aceita.")

    while True:
        request = client_socket.recv(1024).decode("utf-8")

        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"Recebido: {request}")
        response = "Accepted".encode("utf-8")
        client_socket.send(response)

    client_socket.close()
    print("Conexão fechada")
    server.close()
    print("Servidor fechado")

if __name__ == "__main__":
    ip = main()
    print(f"IPv4: {ip}")
    socketMain()
