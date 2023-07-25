# list comprehension -> [expr for item in list]
list = list(range(1, 11))
print("Lista sem list comprehension: ", list)

# list comprehension
list_comprehension = [i * 2 for i in list]
print("Lista com list comprehension multiplicando por 2: ", list_comprehension)

#  list comprehension mapeando uma lista
produtos = [
    {"nome": "p1", "preco": 13},
    {"nome": "p2", "preco": 55.55},
    {"nome": "p3", "preco": 5.59},
    {"nome": "p4", "preco": 22},
]

pessoas = [
    {"nome": "Luiz", "idade": 32},
    {"nome": "Eduarda", "idade": 43},
    {"nome": "Joana", "idade": 65},
    {"nome": "Lucas", "idade": 14},
]

# mapeando uma lista de produtos
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20
    else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep="\n")
