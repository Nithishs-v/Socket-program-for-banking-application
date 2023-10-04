import socket


accounts = {
    'user1': {'balance': 1000},
    'user2': {'balance': 1500}
}

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        command = data.split()
        if command[0] == 'BALANCE':
            username = command[1]
            if username in accounts:
                balance = accounts[username]['balance']
                client_socket.send(str(balance).encode('utf-8'))
            else:
                client_socket.send("Invalid username".encode('utf-8'))
        elif command[0] == 'WITHDRAW':
            username = command[1]
            amount = float(command[2])
            if username in accounts and accounts[username]['balance'] >= amount:
                accounts[username]['balance'] -= amount
                client_socket.send("Transaction successful".encode('utf-8'))
                
            else:
                client_socket.send("Transaction failed".encode('utf-8'))
        else:
            client_socket.send("Invalid command".encode('utf-8'))

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)

    print("Bank server listening on port 8888")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

if __name__ == '__main__':
    main()
