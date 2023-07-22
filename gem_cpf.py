# gerador de cpf valido

import random
import re

from validar_cpf import calcular_primeiro_digito, calcular_segundo_digito


def gerar_cpf() -> str:
    cpf = str(random.randint(100_000_000, 999_999_999))
    cpf += str(calcular_primeiro_digito(cpf))
    cpf += str(calcular_segundo_digito(cpf))
    return cpf


def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'[^0-9]', '', cpf)

    if cpf == cpf[0] * len(cpf) or len(cpf) != 11:
        return False

    primeiro_digito = calcular_primeiro_digito(cpf)
    segundo_digito = calcular_segundo_digito(cpf)
    cpf_gerado = f'{cpf[:9]}{primeiro_digito}{segundo_digito}'
    return cpf == cpf_gerado


if __name__ == '__main__':
    cpf = gerar_cpf()
    cpf_format = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    if validar_cpf(cpf):
        print(f'O CPF {cpf_format} é válido')
    else:
        print(f'O CPF {cpf_format} é inválido')

    print(f'O cpf gerado é {cpf_format}')
