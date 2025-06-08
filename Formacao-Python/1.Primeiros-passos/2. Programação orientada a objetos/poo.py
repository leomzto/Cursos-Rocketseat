# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f'Olá, {self.nome}.'

# Objetos
pessoa1 = Pessoa("Leonardo", 19)
print(pessoa1.nome)
print(pessoa1.idade)
# print(vars(pessoa1)) || print(pessoa1.__dict__)
msg = pessoa1.saudacao()
print(msg)
