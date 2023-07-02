# loop de repetição while

# while executa enquanto a condição for verdadeira

# loop infinito
# condicao = True
# while condicao:
#     print('loop infinito')
# loop infinito com break


# while condicao:
#     nome = input('Digite seu nome: ')
#     print('loop infinito')
#     if nome == 'sair':
#         break
import time

contador = 0

while contador < 10:
    contador += 1
    print(contador, end='\r')
    time.sleep(0.5)
