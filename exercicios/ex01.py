from datetime import datetime

nome: str = input('Digite seu nome: ')
sobrenome: str = input('Digite seu sobrenome: ')
altura: float = float(input('Digite sua altura: '))
ano_atual: int = datetime.now().year
ano_nascimento: int = int(input('Digite seu ano de nascimento: '))
idade: int = ano_atual - ano_nascimento
maior_idade: bool = idade >= 18

print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Altura: {altura}')
print(f'É maior de idade: {maior_idade}')
print(f'Ano de nascimento: {idade}')
