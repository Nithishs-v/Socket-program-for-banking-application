import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8888))

    while True:
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            client_socket.send(f"BALANCE {username}".encode('utf-8'))
            balance = client_socket.recv(1024).decode('utf-8')
            print(f"Your balance: {balance}")
        elif choice == '2':
            username = input("Enter your username: ")
            amount = input("Enter the amount to withdraw: ")
            client_socket.send(f"WITHDRAW {username} {amount}".encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(response)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

    client_socket.close()

if __name__ == '__main__':
    main()
