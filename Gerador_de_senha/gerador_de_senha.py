#4. Gerador de senhas
#Criar um programa que gere senhas aleatórias e seguras, com a possibilidade de escolher o tamanho e os caracteres utilizados.

import random

def gerador_de_senha(tamanho, caracteres):
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    tamanho = int(input("Digite o número referente ao tamanho da senha gerada: "))
    caracteres = input("Informe os caracteres a serem usados na senha: ")

    senha = gerador_de_senha(tamanho, caracteres)
    print(f"Sua nova senha é {senha}")


main()