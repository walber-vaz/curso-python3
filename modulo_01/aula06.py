"""
Conversão de tipos
coerção
type convertion
typecasting
coercion

tipos imutáveis: str, int, float, bool, tuple
"""
# Python e fortemente tipado
print("Conversão de tipos")
print(1 + 1)

# Não pode concatenar string com int
# print("1" + 1)

# conversão de tipos
print("1" + str(1))
print(1 + int("1"))
print(int("1") + int("1"))

# type mostra o tipo da variável
print(type(float("1.1") + float("1.1")))

# bool
print(bool(""))  # string vazia é false
print(bool("0"))  # string com 0 é true
