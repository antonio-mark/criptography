import encrypt
import decrypt

def menu():
    choice = None
    while choice != '3':
        print()
        print("BEM VINDO")
        print()
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            encrypt.enc()
            break
        elif choice == '2':
            decrypt.dec()
            break
        elif choice == '3':
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.\n")

menu()



