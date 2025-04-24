# main.py

from utils import encriptar, desencriptar

print("Bem-vinda ao Encriptador de Mensagens!")
print("1. Encriptar")
print("2. Desencriptar")

opcao = input("Escolhe uma opção (1 ou 2): ")

if opcao == "1":
    msg = input("Digite a mensagem para encriptar: ")
    print("Mensagem encriptada:", encriptar(msg))
elif opcao == "2":
    msg = input("Digite a mensagem encriptada (apenas números): ")
    print("Mensagem desencriptada:", desencriptar(msg))
else:
    print("Opção inválida.")
