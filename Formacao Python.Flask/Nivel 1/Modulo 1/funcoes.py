def saudacao(nome):
    print(f"Olá, {nome}")

def quadrado(numero):
    return pow(numero, 2)

def soma(n1, n2):
    return n1 + n2

print('\nChamando função saudaçao:')
saudacao("Leonardo")

print("\nChamando a função quadrado:")
print(f"5^2 = {quadrado(5)}")

print("\nChamando função soma:")
print(f"5 + 4 = {soma(5, 4)}")



