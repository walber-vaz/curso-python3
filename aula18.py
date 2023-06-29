# formatação de string usando f-string
"""
s = 'string'
d e i = inteiros
f = float

.<numero de casas>f
x e X = hexadecimal
(caracteres) < (alinhamento) > (caracteres) ^ (alinhamento centralizado)
> (alinhamento à direita)
< (alinhamento à esquerda)
^ (alinhamento centralizado)

Sina - + ou -
Ex: 0 > -10,.1f
Conversion flags: !s, !r, !a
"""

var = 'string'
print(f'{var:s}')
print(f'{var:>10s}.')
print(f'{var:<10s}.')
print(f'{var:$^10s}.')
# o sinal de + é usado para mostrar o sinal do número tanto positivo
# quanto negativo
# a vírgula é usada para separar os milhares
print(f'{-1000.00000:+,.2f}')
print(f'{-1000.00000:0=+10,.2f}')

# conversion flags
# !s = str() -> __str__
# !r = repr() -> __repr__
# !a = ascii() -> __ascii__

print(f'{var!s}')
print(f'{var!r}')
print(f'{var!a}')
