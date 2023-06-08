import os
import rsa
import aes

def dec():
    private_key_file = ""

    if not os.path.isfile("y.txt"):
        print("Você precisa do y.txt, k-enc.txt e iv-enc.txt para realizar essa operação.")
        return

    with open("y.txt", 'rb') as file:
        ciphertext = file.read()

    with open("k-enc.txt", 'rb') as file:
        k_enc = file.read()

    with open("iv-enc.txt", 'rb') as file:
        iv_enc = file.read()

    while not os.path.isfile(private_key_file):
        private_key_file = input("Digite sua chave privada (zePR.txt): ")

        if not os.path.isfile(private_key_file):
            print("Arquivo não encontrado!")
            print()    

    k = rsa.decrypt_key_with_private_key(private_key_file, k_enc)
    iv = rsa.decrypt_key_with_private_key(private_key_file, iv_enc)

    plaintext = aes.decrypt(ciphertext, k, iv)

    print()
    print("O texto decifrado é: \n")
    print(plaintext)
    print()

    with open("result.txt", 'w', encoding='utf-8') as f:
        lines = plaintext.split('\n')  # Dividir o texto em linhas
        stripped_lines = [line.strip() for line in lines]  # Remover espaços em branco de cada linha
        cleaned_text = '\n'.join(stripped_lines)  # Juntar as linhas novamente em um único texto

        f.write(cleaned_text)
    
    print("O arquivo result.txt foi gerado e salvou o conteúdo decifrado!")
