from Crypto.PublicKey import RSA



# def key_gen():
#     keypair = RSA.generate(1024)
#     public_key = keypair.publickey()

#     export_private_key(keypair, 'private_key.pem')
#     export_public_key(public_key, 'public_key.pem')

#     priv_key = import_private_key('private_key.pem')
#     pub_key = import_public_key('public_key.pem')

#     return [priv_key, public_key]



"""
    Description: Generate public and private RSA keys
    Parameters: None
    Returns: List of private and public RSA keys
    Reference: https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples
"""
def key_gen2():

    pair = RSA.generate(2048) # generating rsa key pair
    
    priv = [pair.n, pair.d] # assigning private key part
    pub = [pair.n, pair.e] # assigning public key part
    
    return [priv, pub] # returning the private key - public key pair
