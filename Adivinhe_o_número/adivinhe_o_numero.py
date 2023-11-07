#2. Jogo da adivinhação
#Criar um jogo em que o programa escolhe um número aleatório e o jogador deve tentar adivinhar qual é esse número.

import random

def jogo_de_adivinhar():
    numero = random.randint(0, 100)
    tentativas = 5

    print("Bem-vindo ao jogo de adivinhação, tente descobrir o número secreto.")

    while True:
        try:
            palpite = int(input("Digite seu palpite entre 0 e 100: "))
            tentativas -= 1

            if palpite == numero:
                print("Boa! Você acertou o número secreto!")
                break
            elif palpite < numero:
                print("Tente um número maior.")
                print(f"Ainda lhe restam {tentativas} tentativas.")
                if tentativas == 0:
                    print("Suas tentativas se esgotaram, comece novamente!")
                    break
            else:
                print("Tente um número menor.")
                print(f"Ainda lhe restam {tentativas} tentativas.")
                if tentativas == 0:
                    print("Suas tentativas se esgotaram, comece novamente!")
                    break
        except ValueError:
            print("Valor inválido, insira um número válido.")

jogo_de_adivinhar()