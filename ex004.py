'''
Programa que leia qualquer número e mostre o seu fatorial
ex: 5! = 5x4x3x2x1 == 120
'''
from math import factorial
num = int(input('Digite um número: '))
cont = num
f = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{} '.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))