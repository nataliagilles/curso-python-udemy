nome= "Natalia Rodrigues"
altura= 1.52
peso= 42 
imc= peso// (altura*altura)

print(nome, "tem", altura, "de altura pesa", peso, "kg e seu imc é", imc )

#ou pode ser feito assim

linha_1= f'{nome} tem {altura} de altura'
linha_2= f'e tem {peso} quilos e seu imc é'
linha_3= f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
