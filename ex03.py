primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    print(
        f"O primeiro número é maior que o segundo número. {primeiro_numero} > {segundo_numero}"
    )
elif primeiro_numero < segundo_numero:
    print(
        f"O segundo número é maior que o primeiro número. {segundo_numero} > {primeiro_numero}"
    )
elif primeiro_numero == segundo_numero:
    print(f"Os números são iguais. {primeiro_numero} = {segundo_numero}")
elif primeiro_numero >= segundo_numero:
    print(
        f"O primeiro número é maior ou igual ao segundo número. {primeiro_numero} >= {segundo_numero}"
    )
elif primeiro_numero <= segundo_numero:
    print(
        f"O segundo número é maior ou igual ao primeiro número. {segundo_numero} >= {primeiro_numero}"
    )
elif primeiro_numero != segundo_numero:
    print(f"Os números são diferentes. {primeiro_numero} != {segundo_numero}")
else:
    print("Erro.")
