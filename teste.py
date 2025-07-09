nome= input("Digite seu nome: ")
numero_letras= len(nome)

try:
    nome.isdigit()

except:
    print(f"Você digitou um numero e nao uma letra")

if print(f"Seu nome é {nome}"):
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print("Seu nome NÃO contém espaços")
    print(f"Seu nome contém {numero_letras} letras")
