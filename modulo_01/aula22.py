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
# import time

# contador = 0

# while contador < 10:
#     contador += 1
#     print(contador, end='\r')
#     time.sleep(0.5)

# while continue
# while True:
#     nome = input('Digite seu nome: ')
#     if nome == 'sair':
#         break
#     if nome == 'pular':
#         continue
#     print(nome)
qtd_linhas = 5
qtd_colunas = 5

# Para cada linha, imprima 5 colunas
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
