# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]


respostas_certas = 0

for pergunta in perguntas:
    print(f"{pergunta['Pergunta']}")

    for opcao in pergunta["Opções"]:
        print(f"[{opcao}]")

    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == pergunta["Resposta"]:
        print("Você acertou!")
        respostas_certas += 1
    else:
        print("Você errou!")

    print()

qtd_perguntas = len(perguntas)

porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f"Você acertou {respostas_certas} respostas.")
print(f"Sua porcentagem de acerto foi de {porcentagem_acerto}%")
