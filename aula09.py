# concatenação de strings
str_concat = "Python" + " " + "Fundamentos"
print(f"concatenação de strings: {str_concat}")

# repetição de strings
str_repet = "Python" * 3
print(f"repetição de strings: {str_repet}")

# operações com strings
# len() retorna o tamanho da string
str_len = len("Python")
print(f"len() retorna o tamanho da string: {str_len}")

# in verifica se um caractere ou uma string está contida em outra string
str_in = "P" in "Python"
print(
    f"In verifica se um caractere ou uma string está contida em outra string: {str_in}"
)

# not in verifica se um caractere ou uma string não está contida em
# outra string
str_not_in = "P" not in "Python"
print(
    f"Not in verifica se um caractere ou uma string não está contida em outra string: {str_not_in}"
)

# index() retorna o índice de um caractere ou string
str_index = "Python".index("t")
print(f"index() retorna o índice de um caractere ou string: {str_index}")

# count() retorna a quantidade de vezes que um caractere ou
# string aparece em outra string
str_count = "Python".count("y")
print(
    f"count() retorna a quantidade de vezes que um caractere ou string aparece em outra string: {str_count}"
)

# upper() retorna a string em maiúsculo
str_upper = "Python".upper()
print(f"upper() retorna a string em maiúsculo: {str_upper}")

# lower() retorna a string em minúsculo
str_lower = "Python".lower()
print(f"lower() retorna a string em minúsculo: {str_lower}")

# capitalize() retorna a string com a primeira letra em maiúsculo
str_capitalize = "python".capitalize()
print(
    f"capitalize() retorna a string com a primeira letra em maiúsculo: {str_capitalize}"
)


# strip() remove os espaços em branco do início e do fim da string
str_strip = "   Python   ".strip()
print(
    f"strip() remove os espaços em branco do início e do fim da string: {str_strip}"
)

# replace() substitui um caractere ou string por outro caractere ou string
str_replace = "Python".replace("P", "J")
print(
    f"replace() substitui um caractere ou string por outro caractere ou string: {str_replace}"
)

# split() retorna uma lista de strings separadas por um caractere ou string
str_split = "Python Fundamentos".split(" ")
print(
    f"split() retorna uma lista de strings separadas por um caractere ou string: {str_split}"
)

# join() retorna uma string concatenada com uma lista de strings
str_join = " ".join(["Python", "Fundamentos"])
print(
    f"join() retorna uma string concatenada com uma lista de strings: {str_join}"
)

# format() retorna uma string formatada
str_format = "Python {0}".format("Fundamentos")
print(f"format() retorna uma string formatada: {str_format}")
