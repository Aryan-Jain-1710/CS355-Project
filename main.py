import socket

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port
    host = 'localhost'
    port = 12345

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(host, port))

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print('Connected to {}:{}'.format(addr[0], addr[1]))

        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print('Received data:', data)

        # Send a response back to the client
        response = 'Hello from the server!'
        client_socket.send(response.encode())

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    main()



