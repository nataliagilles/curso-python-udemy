while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+ - / *): ")

    numeros_validos = False
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        print("Conversão bem-sucedida!")  # DEBUG
        numeros_validos = True
    except:
        print("Erro na conversão!")       # DEBUG
        numeros_validos = False

    if not numeros_validos:
        print("Um ou ambos números digitados são inválidos. Tente Novamente.")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido. Tente Novamente.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador e tente novamente.")
        continue

 #Fazer as contas (Soma, subtração, divisão e multiplicação)
    if operador == "-":
        print(f'{num1_float} - {num2_float} = {num1_float - num2_float}')
    elif operador == "+":
        print(f'{num1_float} + {num2_float} = {num1_float + num2_float}')
    elif operador == "/":
        print(f'{num1_float} / {num2_float} = {num1_float / num2_float}')
    elif operador == "*":
        print(f'{num1_float} * {num2_float} = {num1_float * num2_float}')



#Para encerrar o programa:
    sair= input ("Você deseja sair [s] sim?:  " ).lower() .startswith('s')
    
    if sair or True:
        break