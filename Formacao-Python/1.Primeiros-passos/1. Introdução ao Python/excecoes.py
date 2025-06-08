print('Exemplo de captura de exceções')
try:
    numero = int(input('Digite um numero inteiro: '))
    resultado = pow(numero, 2)
except ValueError as erro:
    print(f"Erro: ValueErrosf")
    raise ValueError('Tipo de variaveis incompativeis')
except Exception as erro:
    print(f'Erro: {erro}')
else:
    print(f'{numero}^2 = {resultado}')
finally:
    print('Operação finalizada')
