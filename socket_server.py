import socket
from main import hashfile, sim_check
from rsa_gen import key_gen2


def server_program():

    # geting hostname
    host = socket.gethostname()

    print(host)

    # intiating a port number above 1024
    port = 6000

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





    
    # KEY EXCHANGE !!!!
    keys = key_gen2()
    spriv = keys[0]
    spub = keys[1]

    # sending server n and e
    sn = spub[0].to_bytes(1000, 'big')
    se = spub[1].to_bytes(50, 'big')
    print("\nserver pub e as int:")
    print(spub[1])
    print("\nserver pub n as int:")
    print(spub[0])

    print("\n\nSending server details...\n")
    conn.send(sn)
    print("sent server n")
    conn.send(se)
    print("sent server e")

    # receiving client n and e
    print("\n\nReceiving client details...\n")
    ckeyn = conn.recv(1000)
    ckeyn = int.from_bytes(ckeyn, "big")
    print("\nrecd client n:",ckeyn, sep="\n")

    ckeye = conn.recv(50)
    ckeye = int.from_bytes(ckeye, "big")
    print("\nrecd client e:",ckeye, sep="\n")







    # SENDING SERVER FILES
    server_hash_list = []
    for ctr in range(1, 3): 
        client_file = input(f"\n Enter name of File {ctr} --> ") # server inputs file names

        b_hashed_file = hashfile(client_file) # hashing the content of the file inputted
        hashed_file = int.from_bytes(b_hashed_file, "big")
        server_hash_list.append(hashed_file)
        conn.send(b_hashed_file) # sending hashed message to client

        signature = pow(hashed_file, spriv[1], spriv[0]) # creating a signature for the hashed message
        b_sign = signature.to_bytes(256, "big")
        conn.send(b_sign) # sending signature of the hashed message to client
        
        print(f"\n {client_file} file content successfully hashed, signed and sent!\n")







    # RECEIVING CLIENT FILES
    client_hash_list = []
    for ctr in range(1,3): 
        b_clientfile = conn.recv(32)
        clientfile_hash = int.from_bytes(b_clientfile, "big")
        client_hash_list.append(clientfile_hash)

        b_sign = conn.recv(256)
        sign = int.from_bytes(b_sign, "big")
        sign_hash = pow(sign, ckeye, ckeyn)
        
        if not sign_hash == clientfile_hash:
            print("unable to verify.")
            conn.close()
            break






    # SIMILARITY CHECK !!!
    print("List of files recd from client:")
    print(client_hash_list)
    print("\nList of files sent to client:")
    print(server_hash_list)
    
    # checking similarity
    print("\nRunning similarity check...")
    sim_check(server_hash_list, client_hash_list)

    print("\n\n")

    # close the connection
    conn.close()  


if __name__ == '__main__':
    server_program()
