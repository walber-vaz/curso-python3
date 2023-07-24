# Estrutura de dados: Set
# Função: Exemplo de uso do set
def main():
    # Criando um set
    s = set()
    # Adicionando elementos
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(3)
    # Imprimindo o set
    print(s)
    # Verificando se 3 está no set
    print(3 in s)
    # Verificando se 5 está no set
    print(5 in s)
    # Removendo o elemento 2
    s.remove(2)
    # Imprimindo o set
    print(s)
    # Imprimindo o tamanho do set
    print(f"O tamanho do set é {len(s)}")


if __name__ == "__main__":
    main()
