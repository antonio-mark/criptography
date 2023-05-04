import bf
import argparse

parser = argparse.ArgumentParser(description='Este script decodifica mensagens cifradas usando a cifra de Caesar ou Vigenère. Para decodificar, você precisa fornecer o arquivo contendo a mensagem cifrada (ciphered.txt). Você pode escolher entre a cifra de Caesar (-c) ou Vigenère (-v).')

parser.add_argument('-v', '--vigenere', help='Executa o brute force de Vigenere', action='store_true')
parser.add_argument('-c', '--caesar', help='Executa o brute force de Caesar', action='store_true')

args = parser.parse_args()

if args.vigenere:
    bf.vigenere()

if args.caesar:
    bf.caesar()




