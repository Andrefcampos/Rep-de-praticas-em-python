# escrever um programa que extraia somente os números pares de uma lista
from random import randint

numeros = [randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99),
           randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99)]

par = filter(lambda x: x % 2 == 0, numeros)
print(numeros)
print(f'>>> Os números pares são: {list(par)}')
