# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # atributo da classe

    def __init__(self, nome):
        self.nome = nome # atributo da instancia

    def metodo_instancia(self):
        return f'Método de instancia chamado para {self.nome}'

    @classmethod
    def metodo_classe(cls):
        return f'Metodo de classe chamado para valor={cls.valor}'

    @staticmethod
    def metodo_estatico():
        return 'Metodo estatico chamado'


objeto = MinhaClasse(nome='Classe Exemplo')
print(objeto.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(',')
        return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f'Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}')

class Matematica:

    @staticmethod
    def somar(n1, n2):
        return n1 + n2

print(Matematica.somar(5, 10))
