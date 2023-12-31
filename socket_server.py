import socket
from main import hashfile, sim_check2
from rsa_gen import key_gen2



"""
    Description: Implementation of the server-side communication, 
                 involving key exchange and verification, file hashing 
                 and verification by digital signature, and 
                 computation of similarity check results for the client.
    Parameters: None
    Returns: None
    References: https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples # for RSA Digital Signature Implementation
                https://realpython.com/python-sockets/ # for socket programming in python
"""
def server_program():
 
    host = socket.gethostname()    # geting hostname
    port = 6000    # intiating a port number above 1024
    server_socket = socket.socket()    # getting instance of socket
    server_socket.bind((host, port))    # binding host address and port together
    server_socket.listen(1)    # configure how many client the server can listen simultaneously
    conn, address = server_socket.accept()    # accept a connection
    print("\nConnection from: " + str(address)) # when message received from client




    # generating server keys
    server_key_list = key_gen2() # generating rsa key-pair for server
    server_private_key = server_key_list[0] # [n, d]
    server_public_key = server_key_list[1] # [n, e]

    # server public key (n) and (e)
    server_public_key_n = server_public_key[0].to_bytes(1000, 'big')
    server_public_key_e = server_public_key[1].to_bytes(50, 'big')
    





    # SENDING SERVER PUBLIC KEY (n and e)
    print("\nSending Server public key to Client...")
    
    conn.send(server_public_key_n)
    # print("sent server n")
    
    conn.send(server_public_key_e)
    # print("sent server e")






    # VERIFYING SERVER PUBLIC KEY FROM CLIENT
    print("\nReceiving public key for verification...")

    verify_server_key_n = conn.recv(1000)
    verify_server_key_n = int.from_bytes(verify_server_key_n, "big") # converting key from bytes to int
    verify_server_key_e = conn.recv(50)
    verify_server_key_e = int.from_bytes(verify_server_key_e, "big") # converting key from bytes to int

    if verify_server_key_n != server_public_key[0] or verify_server_key_e != server_public_key[1]: # if key received doesn't match key generated
        print("\nKey Verification Failed!")
        print("Closing connection....")
        conn.close()






    # RECEIVING CLIENT PUBLIC KEY (n and e)
    print("\nReceiving Client public key...")

    client_public_key_n = conn.recv(1000)    # receiving client public key (n)
    client_public_key_n = int.from_bytes(client_public_key_n, "big")    # converting (n) from bytes to int

    client_public_key_e = conn.recv(50)    # receiving client public key (e)
    client_public_key_e = int.from_bytes(client_public_key_e, "big")    # converting (e) from bytes to int





    # SENDING CLIENT PUBLIC KEY BACK FOR VERIFICATION
    print("\nVerifying client public key...\n")
    conn.send(client_public_key_n.to_bytes(1000, 'big')) 
    conn.send(client_public_key_e.to_bytes(50, 'big')) 






    # SENDING SERVER FILES !!!
    server_str_list = []
    server_hash_list = []
    
    for ctr in range(1, 6): 
        print("-----------------------------------------------------------------")

        server_file = input(f"\nEnter name of File {ctr} --> ") # server inputs file names
        server_str_list.append(server_file) # adding server file to list of server files

        b_hashed_file = hashfile(server_file) # hashing the content of the file inputted
        conn.send(b_hashed_file) # sending hashed message to client

        hashed_file = int.from_bytes(b_hashed_file, "big") # converting from bytes to int
        server_hash_list.append(hashed_file) # adding hashed message to server's list of hashes
        
        signature = pow(hashed_file, server_private_key[1], server_private_key[0]) # creating a signature for the hashed message
        b_sign = signature.to_bytes(256, "big") # converting signature from int to bytes
        conn.send(b_sign) # sending signature of the hashed message to client
        
        print(f"\n\"{server_file}\" file content successfully hashed, signed and sent!\n")







    # RECEIVING CLIENT FILES !!!
    print("-----------------------------------------------------------------")
    client_hash_list = []
    for ctr in range(1,6): 
        b_clientfile = conn.recv(32) # hashed message as bytes from client
        clientfile_hash = int.from_bytes(b_clientfile, "big")  # converting hashed message from bytes to int
        client_hash_list.append(clientfile_hash)  # adding client's hashed message to the client's list of hashes

        b_sign = conn.recv(256)  # signature of the hashed message as bytes from client
        sign = int.from_bytes(b_sign, "big")  # converting signature from bytes to int
        sign_hash = pow(sign, client_public_key_e, client_public_key_n)  # computing hash from signature
        
        if not sign_hash == clientfile_hash:  # verification check
            print("\nUnable to verify.")
            print("Closing connection...")
            conn.close()
            break






    # RUNNING SIMILARITY CHECK!!!!
    print("\nRunning similarity check...\n")
    server_matches = sim_check2(client_hash_list, server_hash_list)[1]
    print(str(len(server_matches))+" matches found!")


    print("\n-----------------------------------------------------------------")
    print("\nFiles that match with Client:")

    if len(server_matches) > 0:
        for index in server_matches:
            print(server_str_list[index])
    else:
        print("\nNone")

    print("\n-----------------------------------------------------------------")
    print("\nClosing connection...\n")

    # close the connection
    conn.close()  


if __name__ == '__main__':
    server_program()
