'''Programa que tenha:
- uma lista chamada numeros
- duas funções chamadas sorteio() e somaPar()
- A primeira função vai sortear 5 números (coloca-los dentro da lista)
- segunda vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep
def sorteio():
    print(f'Os números sorteados foram: ', end='')
    for i in range(1, 6):
        i = randint(1, 10)
        print(i, end=' ')
        numeros.append(i)
    print('...PRONTO!')
def somaPar():
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(soma)
numeros = []
sorteio()
somaPar()
