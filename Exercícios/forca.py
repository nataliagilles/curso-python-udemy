palavra_secreta = "melancia"
letras_acertadas= ""
tentativas= 0

while True:
    letra_digitada= input("Digite uma letra:  ")

    if len(letra_digitada) >1:
        print("Digite apenas uma letra")
    continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
        
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

    
        else:
            palara_formada += "*"
    print(letra_secreta)