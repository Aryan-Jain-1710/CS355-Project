import socket
from main import hashfile, sim_check
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from rsa_gen import key_gen



def server_program():

    host = socket.gethostname()    # geting hostname
    port = 3000    # intiating a port number above 1024
    server_socket = socket.socket()    # getting instance of socket
    server_socket.bind((host, port))    # binding host address and port together
    server_socket.listen(1)    # configure how many client the server can listen simultaneously
    conn, address = server_socket.accept()    # accept a connection
    print("\nConnection from: " + str(address) + "\n") # when message received from client







    # loop for communication
    # while True:

        # # receive data stream. it won't accept data packet greater than 1024 bytes
        # data_client = conn.recv(2048).decode()
        
        # if not data_client:
        #     # if data is not received break
        #     break

        # print("\n server priv key: " + str(server_keys[0]))

        # # client generating public key and private key
        # # server_key = gen()

        # # server sending public key to client !!
        # # conn.send(server_key.encode())

        # # message = server_keys[1]
        # # send list of hashes to the client !!
        # conn.send(server_keys[1].exportKey(format='PEM', passphrase=None, pkcs=1))

        # # conn.send(message.encode())  
        





    server_keys = key_gen() # rsa key pair for server
    print("\n server priv key: " + str(server_keys[0]))
    print("\n server public key: " + str(server_keys[1]))

    conn.send(server_keys[1].exportKey(format='PEM', passphrase=None, pkcs=1))    # send server public key to client

    client_pubkey = conn.recv(2048)
    # client_pubkey = RSA.importKey(conn.recv(5000), passphrase=None)  # receive data stream. max data packet 5000 bytes        
    print("\n client public key: " + str(client_pubkey))

    client_key = RSA.import_key(client_pubkey)
    print("\n client public key: " + str(client_key))

    client_message = conn.recv(2048).decode()    # recieve the hash message from the client
    print("\n\n\n hash message: " + str(client_message))

    client_sign = conn.recv(2048).decode()    # receive the signature from the client
    print("\n\n\n signature: " + str(client_sign))


    try:
        pkcs1_15.new(client_key).verify(client_message, client_sign)
        print("The signature is valid.")
    except (TypeError):
        print("The signature is not valid.")
    except (ValueError):
        print("The signature is nottttt valid.")







    conn.close()      # close the connection

if __name__ == '__main__':
    server_program()