pessoa = {}

pessoa["nome"] = str(input("Nome: "))
pessoa["idade"] = int(input("Idade: "))
pessoa["email"] = str(input("Email: "))
pessoa["telefone"] = str(input("Telefone: "))

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(f"{chave} = {valor}")
