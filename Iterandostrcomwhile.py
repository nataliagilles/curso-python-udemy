indice= 0
nome= input ("Digite o seu nome:  ")
nome_novo= " "


while indice < len(nome):

    letra= nome [indice]
    nome_novo += f'*{letra}'
    indice += 1
print (nome_novo)
if not nome.isalpha ():
        print ("Digite um nome sem números ou" \
        "caracteres especiais")