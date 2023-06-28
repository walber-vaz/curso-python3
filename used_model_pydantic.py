from pydantic import BaseModel


class Cadastro(BaseModel):
    nome: str
    idade: int
    ativo: bool


class Pessoas(BaseModel):
    pessoas: list[Cadastro]


class AllPessoas(BaseModel):
    all_pessoas: Pessoas


all_pessoas = {
    "all_pessoas": {
        "pessoas": [
            {"nome": "João", "idade": 20, "ativo": True},
            {"nome": "Maria", "idade": 30, "ativo": False},
        ]
    }
}

print(AllPessoas(all_pessoas=all_pessoas))  # type: ignore
