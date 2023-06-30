"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


def is_int():
    num = input("Digite um número inteiro: ")

    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print(f"{num} é par.")
        else:
            print(f"{num} é ímpar.")
    else:
        print("Não é um número inteiro.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


def saudacao():
    hora = input("Digite a hora atual: ")

    if hora.isdigit():
        hora = int(hora)
        if hora < 0 or hora > 23:
            print("Hora inválida.")
        else:
            if hora <= 11:
                print("Bom dia!")
            elif hora <= 17:
                print("Boa tarde!")
            else:
                print("Boa noite!")
    else:
        print("Valor inválido.")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""


def nome():
    nome = input("Digite seu nome: ")

    if len(nome) <= 4:
        print("Seu nome é curto.")
    elif len(nome) <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")


print("1 - Par ou ímpar")
is_int()

print("2 - Saudação")
saudacao()

print("3 - Nome")
nome()
