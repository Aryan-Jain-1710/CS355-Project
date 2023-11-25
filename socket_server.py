import socket
from main import hashfile, sim_check


def server_program():

    # geting hostname
    host = socket.gethostname()

    print(host)

    # intiating a port number above 1024
    port = 5000

    # getting instance of socket
    server_socket = socket.socket()

    # binding host address and port together
    server_socket.bind((host, port))

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)

    # accept a connection
    conn, address = server_socket.accept()

    # when message received from client
    print("\nConnection from: " + str(address) + "\n")



    # loop for communication
    while True:

        # receive data stream. it won't accept data packet greater than 1024 bytes
        data_client = conn.recv(1024).decode()
        
        if not data_client:
            # if data is not received break
            break
        
        # client message template
        print("\n List of client\'s hashed files: " + str(data_client))

        # server list of hashes
        hash_list = []

        # client generating public key and private key
        server_key = gen()

        # server sending public key to client !!
        conn.send(server_key.encode())


        # loop for server to enter file names
        for ctr in range(1,6):

            # server inputs file name
            server_file = input(f"\n Enter name of File {ctr} --> ")

            # hashed output of file content added to list of hashes
            hash_list.append(hashfile(server_file))

            print(f"\n {server_file} file content successfully hashed!")


        # send list of hashes to the client !!
        conn.send(hash_list.encode())  
        
        # checking similarity
        print("\n Running similarity check...")
        check = sim_check(str(data_client), hash_list)

        # print check
        print("\n Client and Server have the same content on hashed files: " + check)

    # close the connection
    conn.close()  


if __name__ == '__main__':
    server_program()