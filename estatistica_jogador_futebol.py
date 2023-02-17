'''Programa que gerencie o aproveitamento de um jogador de futebol
- nome do jogador
- quantas partidas jogou
- quantos gols em cada partida
- adicionar em um dicionário
- incluir total de gols'''
from time import sleep
print('='*40)
print(f'{"FICHA TÉCNICA JOGADOR":^40}')
print('='*40)
jogador = {}
jogador['nome'] = str(input('Nome do jogador: ')).title()
total = int(input(f'Jogador {jogador["nome"]} atuou em quantas partidas? '))
gol = []
print('-'*30)
for i in range(0, total):
    gol.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i +1}? ')))
jogador['gols'] = gol
jogador['total'] = sum(gol)
print('=' * 30)
sleep(1)
for k, v in jogador.items():
    print(f'  - {k}: {v}')
    sleep(1)
print('='*30)
sleep(1)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(gol):
    print(f' => Na partida {i + 1} fez {v} gols.')
    sleep(1)
print(f'No total de {jogador["total"]} gols.')
