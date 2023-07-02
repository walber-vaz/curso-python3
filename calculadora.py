# Desenvolver uma calculadora com as 4 operações básicas usando while

while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operador = input("Digite o operador: (+-/*) ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except ValueError:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números digitados não é válido')
        continue

    operadores_validos = ['+', '-', '*', '/']

    if operador not in operadores_validos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Calculando...')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
    else:
        print('Operação inválida')

    sair = input("Deseja sair? [s]im ou [n]ão: ").lower().startswith("s")
    if sair is True:
        break
