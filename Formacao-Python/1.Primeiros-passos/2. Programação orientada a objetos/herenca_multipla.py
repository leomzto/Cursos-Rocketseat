class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f'{self.nome} esta amamentando.'

class Ave(Animal):
    def voar(self):
        return f'{self.nome} esta voando.'

class Morcego(Mamifero, Ave): # herança multipla
    def emitir_som(self):
        return 'som ultrassônico'

morcego = Morcego(nome='Batman')

# acessando os metodos da classe base Animal:
print(f'Nome do morcego: {morcego.nome}')
print(f'O {morcego.nome} emite {morcego.emitir_som()}')

# acessando os metodos da classe Mamifero:
print(morcego.amamentar())

# acessando os metodos da classe Ave:
print(morcego.voar())
