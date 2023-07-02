nome = "Walber Vaz"

indice = 0
novo_nome = ''
while indice < len(nome):
    novo_nome += f'*{nome[indice]}'
    indice += 1

print(novo_nome + '*')
