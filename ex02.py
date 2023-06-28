nome: str = "Walber Vaz da Silva"
altura: float = 1.79
peso: int = 92
imc: float = peso / (altura**2)

print(f"{nome} tem {altura}m de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc:.2f}.")


def nivel_imc() -> str:
    if imc < 18.5:
        return f"{nome} está abaixo do peso."
    if imc < 25:
        return f"{nome} está com o peso normal."
    if imc < 30:
        return f"{nome} está com sobrepeso."
    if imc < 35:
        return f"{nome} está com obesidade grau 1."
    if imc < 40:
        return f"{nome} está com obesidade grau 2."
    return f"{nome} está com obesidade grau 3."


print(nivel_imc())
