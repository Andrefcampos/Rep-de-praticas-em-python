'''Programa que gerencie o aproveitamento de um jogador de futebol
- nome do jogador
- quantas partidas jogou
- quantos gols em cada partida
- adicionar em um dicionário
- incluir total de gols'''
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
for k, v in jogador.items():
    print(f'  - {k}: {v}')
print('='*30)
print(f'O jogador {jogador["nome"]} jogou {total} partidas e marcou no total {jogador["total"]} gols.')
