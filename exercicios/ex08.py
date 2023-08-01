"""
faça uma lista de compras com listas
o usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com
arrors de indices inexistentes na lista
"""

# Código:
import os


lista_compras = []

while True:
    print('Opções:', end=' ')
    opcao = input("[i]nserir, [r]emover, [l]istar, [s]air: ").lower()

    if opcao == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        item = input('Digite o item a ser inserido: ')
        lista_compras.append(item)
    elif opcao == 'r':
        item = int(input('Digite o item a ser removido: '))
        try:
            del lista_compras[item]
        except IndexError:
            raise IndexError('Índice inválido')
    elif opcao == 'l':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Índice\tItem')
        for item, valor in enumerate(lista_compras):
            print(f'{item}\t{valor}')
    elif opcao == 's':
        print('Saindo...')
        break
    else:
        print('Opção inválida')
