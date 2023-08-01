# Return de funções
def soma(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        return "Não foi possível calcular a soma"


def subtracao(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    else:
        return "Não foi possível calcular a subtração"


def multiplicacao(a, b):
    if type(a) == int and type(b) == int:
        return a * b
    else:
        return "Não foi possível calcular a multiplicação"


def divisao(a, b):
    if type(a) == int and type(b) == int:
        return a / b
    else:
        return "Não foi possível calcular a divisão"


def calculadora(a, b, operador):
    if operador == "+":
        return soma(a, b)
    elif operador == "-":
        return subtracao(a, b)
    elif operador == "*":
        return multiplicacao(a, b)
    elif operador == "/":
        return divisao(a, b)
    else:
        return "Operador inválido"


print(calculadora(10, 2, "+"))
print(calculadora(10, 2, "-"))
print(calculadora(10, 2, "*"))
print(calculadora(10, 2, "/"))
print(calculadora(10, 2, "a"))
