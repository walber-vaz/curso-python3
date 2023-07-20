# for in com list
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# usando ranger para imprimir a lista com indice
for i in range(len(lista)):
    print(i, lista[i])

# imprimindo indice da lista
for i, item in enumerate(lista):
    print(i, item)
