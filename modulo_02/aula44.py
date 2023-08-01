# métodos úteis dos dicionários
# len(dicionario) -> retorna o tamanho do dicionário
# dicionario.keys() -> retorna as chaves do dicionário
# dicionario.values() -> retorna os valores do dicionário
# dicionario.items() -> retorna os itens do dicionário
# dicionario.setdefault(chave, valor) -> retorna o valor da chave, se não existir, cria a chave com o valor
# dicionario.update(dicionario2) -> atualiza o dicionário com o dicionário2
# dicionario.pop(chave) -> remove o item da chave
# dicionario.popitem() -> remove o último item do dicionário
# dicionario.clear() -> limpa o dicionário
# dicionario.copy() -> copia o dicionário
# dicionario.get(chave) -> retorna o valor da chave
dados: dict = {
    "nome": "Walber",
    "idade": 32,
    "cidade": "São Miguel do Guamá",
    "nacionalidade": "Brasileiro",
    "profissao": "Programador",
    "empresa": "Nenhuma",
    "salario": 0.0,
    "endereco": [
        {
            "rua": "Rua 1",
            "numero": 1,
            "bairro": "Centro",
            "cidade": "São Miguel do Guamá",
            "estado": "Pará",
            "pais": "Brasil",
        }
    ],
}

# len
print(len(dados))

# keys
print(dados.keys())

# values
print(dados.values())

# items
print(dados.items())

# setdefault
print(dados.setdefault("sobrenome", "Vaz"))
