from Crypto.Util import Counter
from Crypto.Cipher import AES
import secrets

def encrypt(plaintext_file, choice):
    if choice == '1':
        k = bytes.fromhex(secrets.token_hex(16))
        nonce = bytes.fromhex(secrets.token_hex(16)) #iv

    if choice == '2':
        k = bytes.fromhex(secrets.token_hex(32))
        nonce = bytes.fromhex(secrets.token_hex(16)) #iv
    
    ctr = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))
    cipher = AES.new(k, AES.MODE_CTR, counter=ctr)

    with open(plaintext_file, 'rb') as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(plaintext)
    return k, nonce, ciphertext

def decrypt(ciphertext, key, iv):
    ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()
