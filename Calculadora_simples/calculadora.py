#1. Calculadora simples
#Desenvolver uma calculadora que permita realizar operações básicas, como adição, subtração, multiplicação e divisão.

while True:

    try:
        num1 = float(input("Digite um número: "))
    except ValueError:
        print("Valor de entrada inválido, digite um número.")

    sinal = input("Digite um sinal (+, -, *, /): ")

    try:
        num2 = float(input("Digite outro número: "))
    except ValueError:
        print("Valor de entrada inválido, digite um número.")
        break

    if sinal == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
        break
    elif sinal == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
        break
    elif sinal == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
        break
    elif sinal == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
        break
    else:
        print("Operação inválida, tente novamente!")