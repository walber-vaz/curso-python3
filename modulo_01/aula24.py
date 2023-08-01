frase = (
    'O python é uma linguagem excelente'
    'para quem está começando a programar'
    'e também para quem já programa a anos'
)

indice = 0
ultimo_indice = ''
qtd_vezes_letra = 0

while indice < len(frase):
    letra = frase[indice]

    if letra == ' ':
        indice += 1
        continue

    count_letra = frase.count(letra)

    if qtd_vezes_letra < count_letra:
        qtd_vezes_letra = count_letra
        ultimo_indice = letra

    indice += 1

print(
    f'A letra que apareceu mais vezes é: "{ultimo_indice}"'
    f' e apareceu {qtd_vezes_letra} vezes'
)
