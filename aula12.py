# Função input
# A função input() permite que você pare o programa e espere que o usuário
# digite alguma informação
# Você pode passar uma string como argumento para essa função, para que o
# usuário saiba o que digitar
# O programa vai esperar que o usuário digite alguma coisa e aperte enter
# O que o usuário digitar será retornado pela função input()
# O retorno da função input() é sempre uma string
# Para converter o retorno da função input() para um número inteiro, use a
# função int()
# Para converter o retorno da função input() para um número real, use a função
# float()
# Para converter o retorno da função input() para um número complexo, use a
# função complex()
# Para converter o retorno da função input() para um booleano, use a função
# bool()
# Para converter o retorno da função input() para uma lista, use a função
# list()
# Para converter o retorno da função input() para uma tupla, use a função
# tuple()
# Para converter o retorno da função input() para um conjunto, use a função
# set()
# Para converter o retorno da função input() para um dicionário, use a função
# dict()

# Exemplo 1: input() sem argumentos
# print('Digite seu nome: ')
# nome = input()
# print('Seu nome é', nome)

# Exemplo 2: input() com argumento
nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}')

# Exemplo 3: input() com conversão para inteiro
idade = int(input('Digite sua idade: '))
print(f'Você tem {idade} anos')

# Exemplo 4: input() com conversão para real
altura = float(input('Digite sua altura: ').split()[0].replace(',', '.'))
print(f'Sua altura é {altura:.2f}')

# Exemplo 5: input() com conversão para complexo
complexo = complex(input('Digite um número complexo: (Ex: 1+2j) '))
print(f'O número complexo é {complexo}')

# Exemplo 6: input() com conversão para booleano
booleano = bool(
    input('Digite um valor booleano: (Ex: True/False) ').capitalize()
)
print(f'O valor booleano é {booleano:}')

# Exemplo 7: input() com conversão para lista
lista = list(input('Digite uma lista: (Ex: 1, 2, 3) ').split(','))
print(f'A lista é {lista}')

# Exemplo 8: input() com conversão para tupla
tupla = tuple(input('Digite uma tupla: (Ex: 1, 2, 3) ').split(','))
print(f'A tupla é {tupla}')

# Exemplo 9: input() com conversão para conjunto
conjunto = set(input('Digite um conjunto: (Ex: 1, 2, 3) ').split(','))
print(f'O conjunto é {conjunto}')

# Exemplo 10: input() com conversão para dicionário
dicionario = dict(input('Digite um dicionário: (Ex: 1, 2, 3) ').split(','))  # type: ignore
print(f'O dicionário é {dicionario}')
