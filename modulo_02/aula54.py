# try e except - Tratamento de erros e exceções

try:
    divisor = 0
    produto = 17
    resultado = produto / divisor
    print(f'O resultado da divisão é {resultado}')
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero.')
except NameError:
    print('Variável não definida.')
else:
    print('Executa quando não ocorre exceção.')
finally:
    print('Sempre executa.')
