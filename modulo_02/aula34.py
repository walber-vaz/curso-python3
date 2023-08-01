salas = [
    ["Pedro", "João", "Maria", ["Ana", "Carlos"]],
    ["Miguel", "Ana", "Carlos"],
]

# print(salas[0][3][1])


def list_encadeada(sala):
    for sal in sala:
        for nome in sal:
            if isinstance(nome, list):
                for aluno in nome:
                    print(aluno)
            else:
                print(nome)
        print("----")


list_encadeada(salas)
