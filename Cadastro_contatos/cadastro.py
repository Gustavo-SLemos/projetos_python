#5. Cadastro de contatos
#Desenvolver um programa que permita cadastrar e gerenciar uma lista de contatos, com nome, telefone e e-mail.

lista_de_contatos = []

def cadastrar():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    cadastro = {
        "Nome": nome,
        "Telefone": telefone,
        "Email": email
    }

    lista_de_contatos.append(cadastro)
    print("Contato cadastrado com sucesso")
    
def listar():
    if len(lista_de_contatos) == 0:
        print("Lista sem cadastros")
    else:
        print("Lista de contatos: ")
        for contato in lista_de_contatos:
            print(f"Nome: {contato['Nome']}")
            print(f"telefone: {contato['Telefone']}")
            print(f"email: {contato['Email']}")

while True:
    print("Menu:")
    print("1 - Cadastrar novo contato")
    print("2 - Listar contatos")
    print("3 - Sair")

    opcao = input("Digite a opção 1, 2 ou 3: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Até mais!")
        break
    else:
        print("Opção inválida, tente novamente!")