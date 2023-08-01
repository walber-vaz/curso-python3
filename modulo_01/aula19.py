# fatiamento de strings e bytes
# len() -> retorna o tamanho do objeto
# [start:stop:step] -> start é inclusive, stop é exclusive

ola = 'Olá, mundo!'
print(ola[0])

# fatiamento o final não é incluso
# inicio : fim : passo
print(ola[0:3])
print(ola[4:9])
print(ola[0:9:2])
# se omitir o inicio, o python assume que é o inicio da string
print(ola[:5])
# se omitir o fim, o python assume que é o fim da string
print(ola[2:])

# len() -> retorna o tamanho da string
print(len(ola))
