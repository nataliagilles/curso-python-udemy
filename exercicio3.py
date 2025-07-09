nome= input("Digite seu nome: ")
idade= input("Digite sua idade: ")
numero_letras= len(nome)

if nome.isdigit:
    nome=str(nome)
    print(f"Seu nome é {nome}")
else:
    print("Erro. Você digitou um número e não uma letra")

if idade.isdigit():
    print(f"Sua idade é {idade}")
else:
    print("Você digitou errado")
if print(f"Seu nome invertido é {nome[::-1]}"):

    if " " in nome:
        print("Seu nome contém epaços")
else:
    print("Seu nome NÃO contém espaços")
    print(f"Seu nome contém {numero_letras} letras")
if nome:
    primeiro= nome[0]
    ultimo= nome[-1]
    print(f"A primeira letra do seu nome é {primeiro}")
    print(f"A última letra do seu nome é {ultimo}")
else:
    print("Desculpe, você deixou os campos vazios.")

