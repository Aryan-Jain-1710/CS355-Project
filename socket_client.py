import socket
from main import hashfile, sim_check
from rsa_gen import key_gen2


def client_program():

    # since both codes are running on the same system
    host = socket.gethostname()

    # socket server port number
    port = 6000

    # instantiate a socket
    client_socket = socket.socket()  

    # connecting to server
    client_socket.connect((host, port))






    # KEY EXCHANGE!!!!
    keys = key_gen2()
    cpriv = keys[0]
    cpub = keys[1]

    # receiving server n and e
    print("\n\nReceiving server details....")
    skeyn = client_socket.recv(1000)
    skeyn = int.from_bytes(skeyn, "big")
    skeye = client_socket.recv(50)
    skeye = int.from_bytes(skeye, "big")
    print("\nrecd server n:",skeyn, sep="\n")
    print("\nrecd server e:",skeye, sep="\n")

    # sending client n and e
    print("\n\nSending client details....")
    cn = cpub[0].to_bytes(1000, 'big')
    ce = cpub[1].to_bytes(50, 'big')
    print("\client pub e as int:")
    print(cpub[1])
    print("\client pub n as int:")
    print(cpub[0])
    client_socket.send(cn)
    print("sent client n")
    client_socket.send(ce)
    print("sent client e")







    # RECEIVING SERVER FILES !!!
    server_hash_list =[]
    for ctr in range(1,3): 
        b_servfile = client_socket.recv(32)
        servfile_hash = int.from_bytes(b_servfile, "big")
        server_hash_list.append(servfile_hash)

        b_sign = client_socket.recv(256)
        sign = int.from_bytes(b_sign, "big")
        sign_hash = pow(sign, skeye, skeyn)

        if not sign_hash == servfile_hash:
            print("unable to verify.")
            client_socket.close()
            break
        # print(f"{servfile} received!\n\n")







    # SENDING CLIENT FILES !!!
    client_hash_list = []
    for ctr in range(1,3): 
        client_file = input(f"\n Enter name of File {ctr} --> ") # server inputs file names

        b_hashed_file = hashfile(client_file) # hashing the content of the file inputted
        hashed_file = int.from_bytes(b_hashed_file, "big")
        client_hash_list.append(hashed_file)
        client_socket.send(b_hashed_file) # sending hashed message to client
        
        signature = pow(hashed_file, cpriv[1], cpriv[0]) # creating a signature for the hashed message
        b_sign = signature.to_bytes(256, "big")
        client_socket.send(b_sign) # sending signature of the hashed message to client

        print(f"\n {client_file} file content successfully hashed, signed and sent!\n")







    # RUNNING SIMILARITY CHECK!!!!
    print("List of files recd from server:")
    print(server_hash_list)
    print("\nList of files sent to server:")
    print(client_hash_list)
    
    # checking similarity
    print("\nRunning similarity check...")
    sim_check(server_hash_list, client_hash_list)

    print("\n\n")

    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()