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
        print("\n Message from client: " + str(data_client))
        
        # server gives the filename
        server_file = input('\n Server input ---> ')

        # hashing the file given by server
        data_server = hashfile(server_file)

        # send data to the client
        conn.send(data_server.encode())  
        
        # checking similarity
        check = sim_check(str(data_client), data_server )

        # print check
        print("\n Client and Server have the same content: " + str(check))



    # close the connection
    conn.close()  


if __name__ == '__main__':
    server_program()