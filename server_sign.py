import socket
from main import hashfile, sim_check
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from rsa_gen import key_gen, key_gen2



def server_program():


    host = socket.gethostname()    # geting hostname
    port = 5000    # intiating a port number above 1024
    server_socket = socket.socket()    # getting instance of socket
    server_socket.bind((host, port))    # binding host address and port together
    server_socket.listen(1)    # configure how many client the server can listen simultaneously
    conn, address = server_socket.accept()    # accept a connection
    print("\nConnection from: " + str(address) + "\n") # when message received from client


    server_key_list = key_gen2() # generating rsa key-pair for server
    server_private_key = server_key_list[0] # [n, d]
    server_public_key = server_key_list[1] # [n, e]



    # RECEIVING CLIENT PUBLIC KEY
    client_public_key = []
    client_public_key.append(conn.recv(3000).decode())    # client public key (n)
    client_public_key.append(conn.recv(3000).decode())    # client public key (e)

    print("keys received")

    # SENDING SERVER PUBLIC KEY TO CLIENT
    conn.send(hex(server_public_key[0]).encode())    # sending server public key 'n' to client
    conn.send(hex(server_public_key[1]).encode())    # sending server public key 'e' to client

    print("keys sent")

    print(hex(server_public_key[0]) + "\n" + hex(server_public_key[1]))




    # RECEIVING THE HASHED MESSAGES AND SIGNATURES FROM CLIENT
    client_hash_list = []
    for ctr in range(1):
        client_hashed_msg = conn.recv(3000).decode()    # hashed message from client
        print(int(client_hashed_msg, 0))
        
        client_hash_list.append(int(client_hashed_msg, 0))    # adding client's hashed message to the client's list of hashes
        client_sign = conn.recv(3000).decode()    # signature of the hashed message from client
        hashFromSignature = pow(int(client_sign, 0), int(client_public_key[1], 0), int(client_public_key[0], 0))   # computing hash from signature

        if (int(client_hashed_msg, 0) != hashFromSignature): 
            print("message from client could not be verified")
            print("closing connection.....")
            conn.close()      # close the connection
            break
            

    # SENDING HASHED MESSAGES AND SIGNATURES FROM SERVER TO CLIENT
    server_hash_list = []
    for ctr in range(1):

        server_file = input(f"\n Enter name of File {ctr} --> ") # server inputs file names
        server_hashed_msg = hashfile(server_file) # hashing the content of the file inputted
        # print("hashed output of the file content: " + server_hashed_msg) # showing server their hashed output of the file content
        server_hash_list.append(server_hashed_msg) # adding hashed message to server's list of hashes
        signature = pow(server_hashed_msg, server_private_key[1], server_private_key[0]) # creating a signature for the hashed message
        conn.send(hex(server_hashed_msg).encode()) # sending hashed message to client
        conn.send(hex(signature).encode()) # sending signature of the hashed message to client

        print(f"\n {server_file} file content successfully hashed, signed and sent!")




    # checking similarity
    print("\n Running similarity check...")
    sim_check(server_hash_list, client_hash_list)

    # print check
    # print("\n Client and Server have the same content on hashed files: " + check)



    # message = b'shreyaaaaa is the best'
    # hashed_msg = int.from_bytes(sha512(message).digest(), byteorder='big')

    # hashFromSignature = pow(signature, client_public_key[1], client_public_key[0])
    # print("Signature valid:", hashed_msg == hashFromSignature)
    # print("\nHash From Signature:\n")
    # print(hashFromSignature)

    # client_socket.send(hex(hashed_msg).encode())
    # client_socket.send(hex(signature).encode())


 
    # client_hash_list = []
    # client_hashed_msg = conn.recv(3000).decode()    # hashed message from client


    # # print("\nhashed message:\n ")
    # # print(int(hashed_msg, 0))
    # # print("\n\n\n")

    # sign = conn.recv(3000).decode()    # signature
    # # print("\nsignature: \n")
    # # print(int(sign, 0))
    # # print("\n\n\n")

    # # signature check
    # hashFromSignature = pow(int(sign, 0), int(client_key[1], 0), int(client_key[0], 0))
    # # print("hash from signature: \n")
    # # print(hashFromSignature)
    # # print("\nSignature valid:", int(hashed_msg, 0) == hashFromSignature)



    conn.close()      # close the connection



if __name__ == '__main__':
    server_program()