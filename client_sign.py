import socket
from main import hashfile, sim_check
from rsa_gen import key_gen2, key_gen
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from hashlib import sha512
from Crypto.PublicKey import RSA
import time

def client_program():

    host = socket.gethostname() # since both codes are running on the same system
    port = 5000 # socket server port number
    client_socket = socket.socket()  # instantiate a socket
    client_socket.connect((host, port)) # connecting to server


    client_key_list = key_gen2() # generating rsa key-pair for client
    client_private_key = client_key_list[0] # [n, d]
    client_public_key = client_key_list[1] # [n, e]
    

    print("Client public key:\n")
    print(hex(client_public_key[0]) + "\n" + hex(client_public_key[1]))


    # SENDING CLIENT PUBLIC KEY TO SERVER
    client_socket.send(str(client_public_key[0]).encode())  # sending client public key 'n' to server
    client_socket.send(str(client_public_key[1]).encode())  # sending client public key 'e' to server

    print("\nPublic Keys sent to Server")

    # RECEIVING SERVER PUBLIC KEY
    server_public_key = []
    print("before receiving n from server")
    server_public_key.append(client_socket.recv(3000).decode())    # server public key (n)
    print("before receiving e from server")
    server_public_key.append(client_socket.recv(3000).decode())    # server public key (e)
    print("after receiving both n and e from server")
    
    server_public_key[0] = int(server_public_key[0], 0)
    server_public_key[1] = int(server_public_key[1], 0)

    print("\nPublic Keys received from Server")

    # print(type(client_public_key[0]))
    # print(type(server_public_key[0]))
    
    # print(hex(server_public_key[0]) + "\n" + hex(server_public_key[1]))


    # SENDING HASHED MESSAGES AND SIGNATURES FROM CLIENT TO SERVER
    client_hash_list = [] 
    for ctr in range(1): 
        client_file = input(f"\nEnter name of File {ctr} --> ") # server inputs file names
        hashed_file = hashfile(client_file) # hashing the content of the file inputted
        client_hash_list.append(hashed_file)
        signature = pow(hashed_file, client_private_key[1], client_private_key[0]) # creating a signature for the hashed message
        
        client_socket.send(hex(hashed_file).encode()) # sending hashed message to client
        # print(hashed_file)
        
        client_socket.send(hex(signature).encode()) # sending signature of the hashed message to client

        print(f"\n{client_file} file content successfully hashed, signed and sent!")


    # RECEIVING THE HASHED MESSAGES AND SIGNATURES FROM SERVER
    server_hash_list = []
    for i in range(1):
        server_hash = client_socket.recv(3000).decode()
        server_hash_list.append(int(server_hash, 0))
        server_sign = client_socket.recv(3000).decode()
        sign_hash = pow(int(server_sign, 0), server_public_key[1], server_public_key[0])
        if not (int(server_hash, 0) == sign_hash):
            print("message from server could not be verified")
            print("closing connection.....")
            client_socket.close()      # close the connection
            break


    print(client_hash_list)
    print(server_hash_list)

    # checking similarity
    print("\nRunning similarity check...")
    sim_check(server_hash_list, client_hash_list)

    # print check
    # print("\n Client and Server have the same content on hashed files: " + check)
    
    
    # hashed_msg = int.from_bytes(sha512(message).digest(), byteorder='big')
    # signature = pow(hashed_msg, client_private_key[1], client_private_key[0])
    
    # print("\nhashed message:\n")
    # print(hashed_msg)
    # print("\n Signature:\n")
    # print(signature)

    # message = b'shreyaaaaa is the best'
    # hashed_msg = int.from_bytes(sha512(message).digest(), byteorder='big')

    # hashFromSignature = pow(signature, client_public_key[1], client_public_key[0])
    # print("Signature valid:", hashed_msg == hashFromSignature)
    # print("\nHash From Signature:\n")
    # print(hashFromSignature)

    # client_socket.send(hex(hashed_msg).encode())
    # client_socket.send(hex(signature).encode())



    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()