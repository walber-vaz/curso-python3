# HoF em python


# Função que recebe uma função como parâmetro
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)


print(operacao_aritmetica(soma, 13, 48))
print(operacao_aritmetica(subtracao, 13, 48))


# Função que retorna uma função
def multiplicacao():
    def fn(a, b):
        return a * b

    return fn


def divisao():
    def fn(a, b):
        return a / b

    return fn


print(operacao_aritmetica(multiplicacao(), 13, 48))
print(operacao_aritmetica(divisao(), 13, 48))


# Função que recebe uma função como parâmetro e retorna uma função
def soma_ou_subtracao(fn):
    def fn_interna(a, b):
        return fn(a, b)

    return fn_interna


print(operacao_aritmetica(soma_ou_subtracao(soma), 13, 48))
print(operacao_aritmetica(soma_ou_subtracao(subtracao), 13, 48))
