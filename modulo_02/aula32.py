"""
Imprecisão de ponto flutuante
Double precision floating point number IEEE 754
"""
num1 = 0.1
num2 = 0.7
sum = num1 + num2
print("Sem formatação ->", sum)
print("Usando format ->", f'{sum:.2f}')

# usando round
print("Usando round ->", round(sum, 2))

# usando decimal
# import decimal
# print("Usando decimal ->", decimal.Decimal(sum))
