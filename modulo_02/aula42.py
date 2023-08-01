# Dicionario em python
# Estrutura de dados que armazena valores de um tipo de dado associados a uma chave

# Criando um dicionario
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

# Criando usando dict
dados2: dict = dict(nome="Walber", idade=32, cidade="São Miguel do Guamá")

# Imprimindo o dicionario
print(dados)
print(dados2)

for chave in dados:
    print(f"{chave}: {dados[chave]}")

# Imprimindo o dicionario usando o metodo items()
for chave, valor in dados.items():
    print(f"{chave}: {valor}")
