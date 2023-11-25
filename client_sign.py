import socket
from main import hashfile, sim_check
from rsa_gen import key_gen
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def client_program():

    # since both codes are running on the same system
    host = socket.gethostname()

    # socket server port number
    port = 3000

    # instantiate a socket
    client_socket = socket.socket()  

    # connecting to server
    client_socket.connect((host, port))


    # client generating public key and private key
    # client_key = gen()

    # client sending public key to server
    # client_socket.send(client_key.encode())


    key_list = key_gen()
    client_private_key = key_list[0]
    client_public_key = key_list[1]

    
    client_socket.send(client_public_key.exportKey(format='PEM'))

    print("client public key: \n " + str(client_public_key.exportKey(format='PEM')))

    print("\nclient public key again: " + str(client_public_key))

    # receiving hashed response from server
    data_server = client_socket.recv(2048).decode()

    # server message template
    print('\n Message from server: ' + data_server)

    print("\n client priv key: " + str(client_private_key))

    message = b'shreya is avg not the best'
    hash_msg = SHA256.new(message)
    signature = pkcs1_15.new(client_private_key).sign(hash_msg)

    client_socket.send(hash_msg.hexdigest().encode())
    
    print("\n\n\n hash message: " + hash_msg.hexdigest())
    print("\n\n sign: " + str(signature))

    client_socket.send(str(signature).encode())

    msg2 = b'bye'
    hash2 = SHA256.new(msg2)

    try:
        pkcs1_15.new(client_public_key).verify(hash2, signature)
        print("The signature is valid.")
    except (ValueError, TypeError):
        print("The signature is not valid.")


    # close the connection
    client_socket.close() 


if __name__ == '__main__':
    client_program()