# Generator expression -> E uma forma de criar um generator sem a necessidade
#    de criar uma função, mas sim usando uma sintaxe parecida com a
#    de list comprehension

# Exemplo 1
import sys

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
generator = (n for n in range(1, 10000))
list = [n for n in range(1, 10000)]
print(sys.getsizeof(generator))
print(sys.getsizeof(list))

for n in generator:
    print(n)
