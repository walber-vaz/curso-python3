# closure em python
def criar_saudacao(saudacao, nome):
    def saudar():
        return f"{saudacao} {nome}"

    return saudar


# closure
ola = criar_saudacao("Olá", "Luiz")
print(ola())
