import socket
from main import hashfile, sim_check


def client_program():

    # since both codes are running on the same system
    host = socket.gethostname()

    # socket server port number
    port = 5000

    # instantiate a socket
    client_socket = socket.socket()  

    # connecting to server
    client_socket.connect((host, port))

    # client gives the filename
    client_file = input("\n Client input --> ")  # take input

    # hashing the file given by client
    message = hashfile(client_file)

    # communication loop
    while message.lower().strip() != 'bye':

        # sending the hashed message to server
        client_socket.send(message.encode())

        # receiving hashed respone from server
        data_server = client_socket.recv(1024).decode()

        # server message template
        print('\n Message received from server: ' + data_server)

        # checking similarity
        check = sim_check(str(data_server), message)

        # print check
        print("\n Client and Server have the same content: " + str(check))

        # client gives the filename
        client_file = input("\n Client input --> ")  # take input

        # if client said bye
        if (client_file.lower().strip() == 'bye'):
            break

        # hashing the file given by client
        message = hashfile(client_file)

    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()