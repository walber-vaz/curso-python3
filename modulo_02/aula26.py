from time import sleep

# loop for + range
numeros = range(10)

for numero in numeros:
    sleep(1)
    print(numero, end='\r')
