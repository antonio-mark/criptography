import os
import rsa
import aes

def enc():
    plaintext_file = ""
    choice = None

    name = input("Digite seu nome: ")
    private_key_file, public_key_file = rsa.generate_key_pair(name)
    print(f"Par de chaves gerado: {private_key_file} e {public_key_file}")
    print()

    while not os.path.isfile(plaintext_file):
        plaintext_file = input("Digite o nome do arquivo texto a ser criptografado (x.txt): ")

        if not os.path.isfile(plaintext_file):
            print("Arquivo não encontrado!")
            print()

    while choice != '1' and choice != '2':
        print("Escolha o tamanho da chave:")
        print("1. 128 bits")
        print("2. 256 bits")
        print()
        choice = input("Digite o número da opção desejada (1 ou 2): ")

    k, nonce, ciphertext = aes.encrypt(plaintext_file, choice)

    y = "y.txt"
    with open(y, 'wb') as f:
        f.write(ciphertext)

    print(f"\nTexto cifrado (Y) gerado: {y}")

    k_encrypt_public_key = rsa.encrypt_key_with_public_key(public_key_file, k)
    iv_encrypt_public_key = rsa.encrypt_key_with_public_key(public_key_file, nonce)

    k = "k-enc.txt"
    with open(k, 'wb') as f:
        f.write(k_encrypt_public_key)
    
    iv = "iv-enc.txt"
    with open(iv, 'wb') as f:
        f.write(iv_encrypt_public_key)
    
    print(f"K e IV criptografados com a chave pública gerados: {k} e {iv}")