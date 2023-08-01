# lista em python
string = 'Hello World!'
print(string)

# list e do tipo mutável
lista = [10, 20, 30]  # list(1, 2, 3)
print(lista, type(lista))

metodos_list = [123, 'Walber Vaz', []]
metodos_list[-2] = ''
print(metodos_list[1], type(metodos_list[1]))

# append -> adiciona no final
lista.append(40)
print(lista)

# extend -> adiciona no final
lista.extend([50, 60])
print(lista)

# insert -> adiciona na posição passada no primeiro argumento e segundo
# argumento é a posição
lista.insert(0, 70)
print(lista)

# pop -> remove e retorna o elemento ultimo removido
lista.pop()
print(lista)

# remove -> remove o elemento
lista.remove(70)
print(lista)

# del -> remove o elemento
del lista[0]
print(lista)

# copy -> cria uma cópia
lista_copy = lista[::]
print(lista_copy)

# clear -> remove todos os elementos
lista_copy.clear()
print(lista_copy)
