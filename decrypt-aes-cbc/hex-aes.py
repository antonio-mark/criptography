from Crypto.Cipher import AES
import binascii

# Define a chave e o IV em formato hexadecimal
chave_hex = '73564aaf9167bd9f7d3f847d7bef0e34696e86ff5dd66d5cbf916c6525bf96a3'
iv_hex    = 'c5931a7d97a8e185bd2ac9a3462522a9'

# Converte a chave e o IV para bytes
chave = binascii.unhexlify(chave_hex)
iv = binascii.unhexlify(iv_hex)

# Define o texto cifrado em formato hexadecimal
texto_cifrado_hex = '86E0C4EFC3AE48ABFB6FBCD9668E4AF236DF4AAD3684BDA90896108A02AE83EE'

# Converte o texto cifrado para bytes
texto_cifrado = binascii.unhexlify(texto_cifrado_hex)

# Define o objeto AES com a chave e o modo CBC
aes = AES.new(chave, AES.MODE_CBC, iv)

# Faz o decrypt do texto cifrado
texto_plano = aes.decrypt(texto_cifrado)

# Imprime o texto plano
print(texto_plano.decode())