# Exercicio de funções
# crie funçoes que dubliquem, tripliquem e quadrupliquem um numero
# o numero deve ser passado como parametro


# closure
def mult(x):
    def mult2(y):
        return x * y

    return mult2


# funções
def dobro(x):
    return x * 2


def triplo(x):
    return x * 3


def quadruplo(x):
    return x * 4


# teste
print(dobro(2))
print(triplo(2))
print(quadruplo(2))

# teste closure
print(mult(2)(2))
print(mult(3)(2))
print(mult(4)(2))
