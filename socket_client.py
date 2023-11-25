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




    # client generating public key and private key
    client_key = gen()

    # client sending public key to server
    client_socket.send(client_key.encode())




    # client list of hashes
    hash_list = []

    # loop for client to enter file names
    for ctr in range(1,6):

        # client inputs file name
        client_file = input(f"\n Enter name of File {ctr} --> ")

        # hashed output of file content added to list of hashes
        hash_list.append(hashfile(client_file))

        print(f"\n {client_file} file content successfully hashed!")


    # sending the list of hashed files to server
    client_socket.send(hash_list.encode())




    # receiving hashed response from server
    data_server = client_socket.recv(1024).decode()

    # server message template
    print('\n List of server\'s hashed files: ' + data_server)




    # checking similarity
    print("\n Running similarity check...")
    check = sim_check(str(data_server), hash_list)

    # print check
    print("\n Client and Server have the same content on hashed files: " + check)




    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()