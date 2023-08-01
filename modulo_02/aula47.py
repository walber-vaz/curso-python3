def executa(fun, *args):
    return fun(*args)


# def soma(a, b):
#     return a + b


# def cria_mult(x):
#     def mult(y):
#         return x * y
#
#     return mult


# Mesma coisa da função soma
print(executa(lambda x, y: x + y, 1, 2))

# Mesma coisa da função cria_mult
print(executa(lambda m: lambda n: n * m, 2)(3))
