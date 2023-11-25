import socket
from main import hashfile, sim_check


def client_program():

    # since both codes are running on the same system
    host = socket.gethostname()

    # socket server port number
    port = 3000

    # instantiate a socket
    client_socket = socket.socket()  

    # connecting to server
    client_socket.connect((host, port))


    # client generating public key and private key
    # client_key = gen()

    # client sending public key to server
    # client_socket.send(client_key.encode())


    message = "shreya is not the best"
    client_socket.send(message.encode())


    # receiving hashed response from server
    data_server = client_socket.recv(1024).decode()

    # server message template
    print('\n Message from server: ' + data_server)


    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()