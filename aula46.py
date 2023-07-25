# funções lammada ou funções anônimas
list = [
    {"name": "Lucas", "age": 20},
    {"name": "João", "age": 18},
    {"name": "Maria", "age": 25},
    {"name": "José", "age": 30},
]

# lambda
# list.sort(key=lambda item: item["age"])

# criando uma nova lista com soted
new_list = sorted(list, key=lambda item: item["age"])

print(list)

print(new_list)
