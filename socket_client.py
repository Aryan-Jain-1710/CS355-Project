import socket


def client_program():

    # since both codes are running on the same system
    host = socket.gethostname()

    # socket server port number
    port = 5000

    # instantiate a socket
    client_socket = socket.socket()  

    # connecting to server
    client_socket.connect((host, port))

    # input message template
    message = input("\n Client input --> ")  # take input

    # communication loop
    while message.lower().strip() != 'bye':

        # sending message to server
        client_socket.send(message.encode())

        # receiving respone from server
        data = client_socket.recv(1024).decode()

        # server message template
        print('\n Message received from server: ' + data)

        # client input message template
        message = input("\n Client input --> ")

    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()