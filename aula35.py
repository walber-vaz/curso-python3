# desempacotamento em funções -> uso do asterisco para desempacotar os valores
# de uma lista, tupla ou string e passar como argumento para uma função

strings = ['um', 'dois', 'três']
lista = ["Pedro", "João", "Maria"]
tuplas = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def imprime_strings(*args: str) -> None:
    for i in args:
        print(i)


def imprime_lista(*args):
    for i in args:
        print(i)


def imprime_tuplas(*args):
    for i in args:
        print(i)


imprime_strings(*strings)
imprime_lista(*lista)
imprime_tuplas(*tuplas)
