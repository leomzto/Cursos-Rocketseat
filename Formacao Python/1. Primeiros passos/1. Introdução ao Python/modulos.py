print('Exemplo de importação de um modulo padrão:')
# import <modulo> ----> importa todo o modulo
import math
raiz_quadrada = math.sqrt(25)
print(f'A raiz quadrada de 25 é {raiz_quadrada}')

# from <modulo> import <funçãoX, funçãoY>
from math import sqrt
raiz_quadrada = sqrt(144)
print(f'A raiz de 144 é {raiz_quadrada}')

############

print('\nExemplo de criação e utilização de um modulo personalizado:')
"""
crie um .py com as funçoes, depois, use:
import <modulo criado>
"""
import meu_modulo # ou from meu_modulo import <funçãoX, funçãoY>
saudacao = meu_modulo.saudacao('Leonardo')
dobro = meu_modulo.dobro(10)
print(saudacao)
print(f'O dobro de 10 é {dobro}')

############

print('\nExemplo de importação de um modulo de terceiro:')
""""
site: pypi.org (busca por modulos de terceiros)
Para utilizar de modulos de terceiros
deve-se instalar usando o pip install
depois de instalar, usar o import normalmente
EXEMPLO: para usar o "requests":
no terminal:
pip install requests ## ou pip3
no arquivo:
import requests ou from requests import <funcionalidade(s)>
"""
import requests
url = "https://www.example.com"
response = requests.get(url)
print(f'Status da requisição de {url}: {response}')

