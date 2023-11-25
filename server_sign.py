import socket
from main import hashfile, sim_check


def server_program():

    # geting hostname
    host = socket.gethostname()

    # intiating a port number above 1024
    port = 3000

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
            
        print(data_client)


        # client generating public key and private key
        # server_key = gen()

        # server sending public key to client !!
        # conn.send(server_key.encode())

        message = "bob is best"
        # send list of hashes to the client !!
        conn.send(message.encode())  
        
        
    # close the connection
    conn.close()  


if __name__ == '__main__':
    server_program()