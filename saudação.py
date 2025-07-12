try:
    hora= int (input ("Que horas são?:  "))
    if hora < 0 or hora > 23:
        print ("Hora invélida. Digite um número de" \
        "0 até 23.")
    elif hora <= 11:
        print ("Bom Dia!")
    elif hora <= 17:
        print ("Boa Tarde!")
    else:
        print ("Boa Noite!")
except:
    print(" Por favor digite um número válido")
