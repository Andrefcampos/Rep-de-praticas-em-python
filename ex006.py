'''Programa que aprimore o desafio 93
- funcione com vários jogadores
- incluindo um sistema de visualização detalhada do aproveitamento de cada jogador'''
ficha_jogadores = []
gols = []
jogador = {}
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    jogador['partidas'] = int(input(f'Quantas partidas o jogador {jogador["nome"]} atuou? '))
    for g in range(0, jogador['partidas']):
        gols.append(int(input(f'O jogador {jogador["nome"]} marcou quantos gols na {g+1}ª partida: ')))
    jogador['gols'] = gols[:]
    gols.clear()
    ficha_jogadores.append(jogador.copy())
    while True:
        exit = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if exit in 'SN':
            break
        print('Valor inválido, digite "S" ou "N".')
    if exit == 'N':
        break
print(ficha_jogadores)
print('='*40)
