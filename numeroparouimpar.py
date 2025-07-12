
try:
    numero= int (input ("Digite um número:  "))
    if numero % 2==0:
        print (f"O numero {numero} é Par")
    else:
        print (f"O numero {numero} é impar")

except:
    print (" Por favor digite um número inteiro")
