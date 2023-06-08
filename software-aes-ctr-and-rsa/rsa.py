from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair(name):
    key = RSA.generate(2048)
    
    private_key = key.export_key()
    private_key_file = f"{name}PR.txt"
    with open(private_key_file, 'wb') as f:
        f.write(private_key)
    
    public_key = key.publickey().export_key()
    public_key_file = f"{name}PU.txt"
    with open(public_key_file, 'wb') as f:
        f.write(public_key)
    
    return private_key_file, public_key_file

def encrypt_key_with_public_key(public_key_file, key):
    with open(public_key_file, 'rb') as file:
        public_key = RSA.import_key(file.read())
    
    cipher_rsa = PKCS1_OAEP.new(public_key)
    
    encrypted_key = cipher_rsa.encrypt(key)
    
    return encrypted_key

def decrypt_key_with_private_key(private_key_file, encrypted_key):
    with open(private_key_file, 'rb') as file:
        private_key = RSA.import_key(file.read())
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    
    decrypted_key = cipher_rsa.decrypt(encrypted_key)
    
    return decrypted_key