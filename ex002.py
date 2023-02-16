'''Programa onde 4 jogadores joguem dado e tenha resultados em um dicionario.
- no final coloque esse dicionário em ordem;
(sabendo que o vencedor tirou o maior número do dado).'''
from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in jogadas.items():
    print(f'É a vez do {k}: jogou o dado...', end='')
    sleep(2)
    print(f'caiu no número {v}.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
