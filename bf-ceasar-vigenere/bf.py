import itertools
from utils import regex 
from utils import generatekey
from files import file

(encrypted_message, bf_list) = file.get_files()

bf_list = [regex.remove_combining_regex(item) for item in bf_list]

def vigenere():
    decrypted_message = ''
    results = []
    while decrypted_message not in bf_list: 
        for combination in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat = 3):
            decrypted_message = ''
            combination_str = ''.join(combination)
            key = generatekey.generate_key(encrypted_message, combination_str)
            key_length = len(key)
            key_as_int = [ord(i) for i in key]
            ciphertext_int = [ord(i) for i in encrypted_message]
            for i in range(len(ciphertext_int)):
                value = (ciphertext_int[i] - key_as_int[i % key_length] - 97) % 26
                decrypted_message += chr(value + 97)
            results.append([decrypted_message, combination_str])
            if decrypted_message in bf_list:
                print('\nMENSAGEM DECIFRADA: {}\nCHAVE: {}'.format(decrypted_message, combination_str))
                print('\narquivo history.txt gerado!')
                for result in results:
                    file.write(result[0], result[1])
                break

def caesar():
    decrypted_message = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 1
    while decrypted_message not in bf_list:
        decrypted_message = ''
        for char in encrypted_message:
            index = alphabet.find(char)
            if index == -1:
                decrypted_message += char
            else:
                new_index = index - key
                new_index = new_index % len(alphabet)
                decrypted_message += alphabet[new_index:new_index+1]
        print('A palavra decifrada foi {} com a chave {}'.format(decrypted_message, key))
        if decrypted_message in bf_list:
            print('\nMENSAGEM CORRETA: {}'.format(decrypted_message))
            print('CHAVE UTILIZADA: {}'.format(key))
        key += 1
