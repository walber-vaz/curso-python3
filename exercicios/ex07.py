"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


import os


secret_word = "python"
letter_acert = []
accert = 0

print("Tente adivinhar a palavra secreta!")
print(f"A palavra secreta tem {len(secret_word)} letras")

while True:
    letter_digit = input("Digite uma letra: ")
    accert += 1

    if len(letter_digit) > 1:
        print("Digite apenas uma letra!")
        continue

    if letter_digit in secret_word:
        letter_acert.append(letter_digit)

    str_format = ""
    for letter in secret_word:
        if letter in letter_acert:
            str_format += letter
        else:
            str_format += "*"

    print(str_format)
    if str_format == secret_word:
        os.system("clear")
        print("Você acertou!")
        print(f"Você acertou a palavra secreta: {secret_word}")
        print(f"Você tentou {accert} vezes")

        str_format = ""
        letter_acert = []

        break
