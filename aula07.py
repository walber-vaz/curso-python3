# variaveis e boas praticas no python

# Varias em python sao dinamicas, ou seja, nao precisam ser declaradas
# antes de serem usadas. O tipo da variavel e determinado pelo valor
# que ela recebe. Para declarar uma variavel, basta atribuir um valor
# a ela. O tipo da variavel pode ser alterado a qualquer momento. Poder
# tipar uma variavel e uma boa pratica de programacao, pois ajuda a
# evitar erros e facilita a leitura do codigo.
# Para colocar nome em uma variavel, deve-se seguir algumas regras:
# 1. O nome da variavel deve comecar com uma letra ou um underline
# 2. O nome da variavel nao pode comecar com um numero
# 3. O nome da variavel pode conter apenas letras, numeros e underlines
# 4. O nome da variavel e case-sensitive, ou seja, nome e Nome sao variaveis
#    diferentes
# 5. Nomes de variaveis podem comecar com letras minusculas e devem seguir
#    o padrao snake_case, ou seja, se o nome da variavel for composto por
#    mais de uma palavra, deve-se separar as palavras por underlines
# 6. Nomes de variaveis que comecam com letras maiusculas sao usadas para
#    classes
# 7. Nomes de variaveis que comecam e terminam com dois underlines sao
#    reservadas para o python, como por exemplo __init__
# 8. Nomes de variaveis que comecam com um underline sao usadas para
#    variaveis privadas, ou seja, variaveis que nao devem ser acessadas
#    diretamente
# 9. Nomes de variaveis que comecam e terminam com dois underlines sao
#    usadas para variaveis magicas, ou seja, variaveis que tem um
#    significado especial no python

nome_completo: str = 'Walber Vaz da Silva'
idade: int = 30
altura: float = 1.75
e_maior_idade: bool = idade >= 18
peso: float = 80

print(f'Nome: {nome_completo}')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'E maior: {e_maior_idade}')
print(f'IMC: {peso / altura ** 2:.2f}')
