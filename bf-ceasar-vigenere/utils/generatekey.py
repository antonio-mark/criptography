def generate_key(string, key):
    key = list(key)
    key_length = len(key)
    string_length = len(string)
    
    if string_length == key_length:
        return ''.join(key)
    else:
        key *= (string_length // key_length) + 1
        key = key[:string_length]  
        return ''.join(key)