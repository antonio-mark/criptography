from Crypto.Cipher import AES
import base64

# Define a chave e o IV em formato base64
chave_b64 = b'c1ZKr5FnvZ99P4R9e+8ONGluhv9d1m1cv5FsZSW/lqM='
iv_b64    = b'xZMafZeo4YW9KsmjRiUiqQ=='

# Converte a chave e o IV para bytes
chave = base64.b64decode(chave_b64)
iv = base64.b64decode(iv_b64)

# Define o texto cifrado em formato base64
texto_cifrado_b64 = b'huDE78OuSKv7b7zZZo5K8jbfSq02hL2pCJYQigKug+4='

# Converte o texto cifrado para bytes
texto_cifrado = base64.b64decode(texto_cifrado_b64)

# Define o objeto AES com a chave e o modo CBC
aes = AES.new(chave, AES.MODE_CBC, iv)

# Faz o decrypt do texto cifrado
texto_plano = aes.decrypt(texto_cifrado)

# Imprime o texto plano
print(texto_plano.decode())