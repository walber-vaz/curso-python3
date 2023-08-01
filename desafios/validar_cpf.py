"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


def calcular_primeiro_digito(cpf: str) -> int:
    """
    Calculates the first digit of a given CPF number.

    Args:
        cpf (str): The CPF number to calculate the first digit for.

    Returns:
        int: The calculated first digit of the CPF number.
    """
    soma = sum(int(digito) * (10 - i) for i, digito in enumerate(cpf[:9]))
    resultado = (soma * 10) % 11
    return 0 if resultado > 9 else resultado


def calcular_segundo_digito(cpf: str) -> int:
    """
    Calculates the second digit of a Brazilian CPF
        (Cadastro de Pessoas Físicas) number.

    Parameters:
    - cpf (str): The CPF number as a string.

    Returns:
    - int: The calculated second digit of the CPF number.
    """
    soma = sum(int(digito) * (11 - i) for i, digito in enumerate(cpf[:10]))
    resultado = (soma * 10) % 11
    return 0 if resultado > 9 else resultado
