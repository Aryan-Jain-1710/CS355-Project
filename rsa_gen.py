from Crypto.PublicKey import RSA


def export_private_key(private_key, filename):

    with open(filename, "wb") as file:
        file.write(private_key.exportKey('PEM', 'MyPassphrase'))
        file.close()


def export_public_key(public_key1, filename):

    with open(filename, "wb") as file:
        file.write(public_key1.exportKey('PEM'))
        file.close()


def import_private_key(filename):

    with open(filename, "rb") as file:
        private_key = RSA.importKey(file.read(), 'MyPassphrase')

    return private_key


def import_public_key(filename):

    with open(filename, "rb") as file:
        public_key1 = RSA.importKey(file.read())

    return public_key1


def key_gen():
    keypair = RSA.generate(2048)
    public_key = keypair.publickey()

    export_private_key(keypair, 'private_key.pem')
    export_public_key(public_key, 'public_key.pem')

    priv_key = import_private_key('private_key.pem')
    pub_key = import_public_key('public_key.pem')

    return [priv_key, publ_key]


def key_gen2():
    
