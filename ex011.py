'''Programa que ajuda um jogador da mega-sena a criar palpites
- programa irá perguntar quantos jogas serão jogados
- sortear 6 numeros de 1 a 60 para cada jogo
- cadastrar tudo em uma lista composta'''
from random import randint
from time import sleep
print('='*30)
print(f'{"JOGOS DA MEGA SENA":^30}')
print('='*30)
lista = []
jogos = []
tot = 1
quant = int(input('Quantos jogos deseja fazer? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '=-'*3)
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
print(f'{"BOA SORTE!":=^31}')
