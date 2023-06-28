# precedência de operadores
# 1º: ()
# 2º: **
# 3º: *
# 4º: /
# 5º: +
# 6º: -
# 7º: =

# Exemplo 1
# Vai imprimir 11, pois primeiro ele vai fazer a multiplicação e depois a soma
print(5 + 3 * 2)

# Exemplo 2
# Vai imprimir 16, pois primeiro ele vai fazer a soma e depois a multiplicação
print((5 + 3) * 2)

# Exemplo 3
# Vai imprimir 5.0, pois primeiro ele vai fazer a divisão e depois a multiplicação
print(5 / 2 * 2)

# Exemplo 4
# Vai imprimir 5.0, pois primeiro ele vai fazer a multiplicação e depois a divisão
print(5 * 2 / 2)

# Exemplo 5
# Vai imprimir 1.25, pois primeiro ele vai fazer a divisão e depois a multiplicação
print(5 / (2 * 2))
