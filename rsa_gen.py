from Crypto.PublicKey import RSA



# def key_gen():
#     keypair = RSA.generate(1024)
#     public_key = keypair.publickey()

#     export_private_key(keypair, 'private_key.pem')
#     export_public_key(public_key, 'public_key.pem')

#     priv_key = import_private_key('private_key.pem')
#     pub_key = import_public_key('public_key.pem')

#     return [priv_key, public_key]


def key_gen2():
    pair = RSA.generate(2048)
    
    priv = [pair.n, pair.d]
    pub = [pair.n, pair.e]
    
    return [priv, pub]
