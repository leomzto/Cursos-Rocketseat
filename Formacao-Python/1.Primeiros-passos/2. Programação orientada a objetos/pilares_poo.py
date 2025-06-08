#Pilares: herança | Polimorfismo | Encapsulamento e Abstração
# Exemplo de herança
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    def andar(self):
        print(f'O animal {self.nome} andou.')
        return
    def emitir_som(self):
        pass
class Cachorro(Animal): #classe filha, herda classe mae
    def emitir_som(self):
        return 'Au, au'
class Gato(Animal):
    def emitir_som(self):
        return 'Miau'
dog = Cachorro('Rex','Cachorro')
cat = Gato('Felix', 'Gato')

# Exemplo de Polimorfismo
print('\nExemplo de polimorfismo:')
animais = [dog, cat]
for animal in animais:
    print(f'O {animal.nome} é um {animal.especie} faz {animal.emitir_som()}')

# Exemplo de Encapsulamento
print('\nExemplo de encapsulamento:')
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo privado "__"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    def consultar_saldo(self):
        return self.__saldo
conta = ContaBancaria(saldo=1000)
print(f'Saldo disponível: {conta.consultar_saldo()}')
conta.depositar(valor=500)
print(f'Saldo disponível: {conta.consultar_saldo()}')
conta.depositar(valor=-500) # nao funciona pois é negativo, nao altera
print(f'Saldo disponível: {conta.consultar_saldo()}')
conta.sacar(valor=2000) # nao funciona pois é maior q o saldo
print(f'Saldo disponível: {conta.consultar_saldo()}')

# Exemplo de Abstração
print('\nExemplo de abstração:') # molde para outras classes
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod # isso é um decorador "@"
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo): # todos os metodos devem ser implementados
    def __init__(self):
        pass
    def ligar(self):
        return 'Carro ligado'
    def desligar(self):
        return 'Carro desligado'

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
