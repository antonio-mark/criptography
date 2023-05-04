def generate_key(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length] - 97) % 26
        ciphertext += chr(value + 97)
    return ciphertext

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length] - 97) % 26
        plaintext += chr(value + 97)
    return plaintext 

if __name__ == "__main__": 
  string = input("Enter the message: ")
  keyword = input("Enter the keyword: ")
  key = generate_key(string, keyword) 
  encrypt_text = encrypt(string,key) 
  print("Encrypted message:", encrypt_text) 
  print("Decrypted message:", decrypt(encrypt_text, key)) 