try:
    nome= input ("Digite seu nome: ")
    tamanho_do_nome= len(nome)
    if not nome.isalpha ():
        print ("Digite um nome sem números ou" \
        "caracteres especiais")
    elif tamanho_do_nome == 0:
        print ("Digite um nome válido")
    elif tamanho_do_nome <= 4:
        print ("Seu nome é curto")
    elif tamanho_do_nome <6:
        print ("Seu nome é normal")
    else:
        print("Seu nome é grande")
except:
    print ("Ocorreu um erro inesperado.")