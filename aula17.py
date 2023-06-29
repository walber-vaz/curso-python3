"""
Interpolação básica de strings

s = 'string'
d e i = inteiros
f = float
x e X = hexadecimal
"""
nome: str = 'Walber Vaz'
preco = 100.00
variavel = '%s, o preço é R$ %.2f' % (nome, preco)

print(variavel)
# Hexadecimal pode ser maiúsculo ou minúsculo (x ou X)
# se quisermos que o número hexadecimal tenha 4 dígitos, colocamos
# 04 antes do x ou X
print(f'O hexadecimal de 10 é {15:04X}')
