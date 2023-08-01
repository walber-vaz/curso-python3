# Operador lógico: and, or, not
# and: verdadeiro se as duas condições forem verdadeiras
# or: verdadeiro se uma das condições for verdadeira
# not: inverte o valor lógico

# Exemplo 1:
numero1 = 2
numero2 = 3

if numero1 > 1 and numero2 > 1:
    print("Os dois números são maiores que 1.")
else:
    print("Pelo menos um dos números é menor que 1.")


# Exemplo 2 or
# or só é falso se as duas condições forem falsas
numero1 = 5
numero2 = 3

if numero1 > 1 or numero2 > 1:
    print("Pelo menos um dos números é maior que 1.")
else:
    print("Os dois números são menores que 1.")


# Exemplo 3 not
# not inverte o valor lógico
numero1 = 1
numero2 = 1

if not numero1 > 1:
    print("O número 1 é menor que 1.")
else:
    print("O número 1 é maior que 1.")
