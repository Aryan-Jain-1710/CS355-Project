import socket
from main import hashfile, sim_check2
from rsa_gen import key_gen2


def client_program():

    host = socket.gethostname() # since both codes are running on the same system
    port = 5000 # socket server port number
    client_socket = socket.socket()  # instantiate a socket
    client_socket.connect((host, port)) # connecting to server






    # generating client keys
    client_key_list = key_gen2() # generating rsa key-pair for client
    client_private_key = client_key_list[0] # [n, d]
    client_public_key = client_key_list[1] # [n, e]

    # client public key (n) and (e)
    client_public_key_n = client_public_key[0].to_bytes(1000, 'big')
    client_public_key_e = client_public_key[1].to_bytes(50, 'big')






    # RECEIVING SERVER PUBLIC KEY (n and e)
    print("\nReceiving Server public key...")

    server_public_key_n = client_socket.recv(1000)    # receiving server public key (n)
    server_public_key_n = int.from_bytes(server_public_key_n, "big")    # converting (n) from bytes to int
    
    server_public_key_e = client_socket.recv(50)    # receiving server public key (e)
    server_public_key_e = int.from_bytes(server_public_key_e, "big")    # converting (e) from bytes to int
    
    # print("\nrecd server n:",skeyn, sep="\n")
    # print("\nrecd server e:",skeye, sep="\n")






    # SENDING CLIENT PUBLIC KEY (n and e)
    print("\nSending Client public key to Server...\n")

    # print("\nclient pub e as int:")
    # print(cpub[1])
    # print("\nclient pub n as int:")
    # print(cpub[0])

    client_socket.send(client_public_key_n)
    # print("sent client n")

    client_socket.send(client_public_key_e)
    # print("sent client e")







    # RECEIVING SERVER FILES !!!
    server_hash_list = []
    for ctr in range(1,3): 
        b_servfile = client_socket.recv(32) # hashed message as bytes from server
        serverfile_hash = int.from_bytes(b_servfile, "big")  # converting hashed message from bytes to int
        server_hash_list.append(serverfile_hash)  # adding server's hashed message to the server's list of hashes

        b_sign = client_socket.recv(256)  # signature of the hashed message as bytes from server
        sign = int.from_bytes(b_sign, "big")  # converting signature from bytes to int
        sign_hash = pow(sign, server_public_key_e, server_public_key_n)  # computing hash from signature

        if not sign_hash == serverfile_hash:  # verification check
            print("\nUnable to verify.")
            print("Closing connection...")
            client_socket.close()
            break
        # print(f"{servfile} received!\n\n")







    # SENDING CLIENT FILES !!!
    client_hash_list = []
    client_str_list = []
    for ctr in range(1,3): 
        print("-----------------------------------------------------------------")

        client_file = input(f"\nEnter name of File {ctr} --> ") # server inputs file names
        client_str_list.append(client_file) # adding client file to list of client files

        b_hashed_file = hashfile(client_file) # hashing the content of the file inputted
        client_socket.send(b_hashed_file) # sending hashed message to client

        hashed_file = int.from_bytes(b_hashed_file, "big") # converting from bytes to int
        client_hash_list.append(hashed_file) # adding hashed message to client's list of hashes
        
        signature = pow(hashed_file, client_private_key[1], client_private_key[0]) # creating a signature for the hashed message
        b_sign = signature.to_bytes(256, "big") # converting signature from int to bytes
        client_socket.send(b_sign) # sending signature of the hashed message to client

        print(f"\n\"{client_file}\" file content successfully hashed, signed and sent!\n")







    # RUNNING SIMILARITY CHECK!!!!
    print("-----------------------------------------------------------------")
    print("\nRunning similarity check...\n")
    client_matches = sim_check2(client_hash_list, server_hash_list)[0]
    
    print("\n-----------------------------------------------------------------")
    print("\nFiles that match with Client:")

    if len(client_matches) > 0:
        for index in client_matches:
            print(client_str_list[index])
    else:
        print("\nNone")

    print("\n-----------------------------------------------------------------")
    print("\nClosing connection...\n")

    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()