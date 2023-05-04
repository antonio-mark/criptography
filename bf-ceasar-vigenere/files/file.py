def get_files():
    cipher_txt = open('files/ciphered.txt', encoding='utf8')
    encrypted_message = cipher_txt.readline()
    cipher_txt.close()
    list_bf = open('files/list.txt', encoding='utf8')
    bf_list = list_bf.readlines()
    list_bf.close()
    return (encrypted_message, bf_list)

def write(decrypted_message, combination_str):
    file_write = open('history.txt', 'a')
    file_write.write('{}, {}'.format(decrypted_message, combination_str) + '\n')
    file_write.flush()
    file_write.close()