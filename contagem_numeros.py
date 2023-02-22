'''Programa que tenha uma função contador():
- que receba três parâmetros: inicio, fim e passo;
- relize a contagem;
- programa tem que realizar três contagens através da função
- a. de 1 a 10, de 1 em 1
- b. de 10 a 0, de 2 em 2
- c. uma contagem personalizada.'''
from time import sleep
def contador(i, f, p):
    if i > f:
        p = -p
    if p == 0:
        p = 1
    print(f'Contagem de {i} a {f} de {p} em {p}: ', end='')
    for x in range(i, f, p):
        print(x, ' ', end='')
        sleep(0.5)
    print()
    print('-'*40)
contador(1, 10, 1)
contador(10, 1, 2)
print('Agora é sua vez... faça sua contagem.')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
