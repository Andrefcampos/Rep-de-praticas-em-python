'''Programa que aprimore o desafio 93
- funcione com vários jogadores
- incluindo um sistema de visualização detalhada do aproveitamento de cada jogador'''
ficha_jogadores = []
gols = []
jogador = {}
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    try:
        jogador['partidas'] = int(input(f'Quantas partidas o jogador {jogador["nome"]} atuou? '))
    except:
        continue
    for g in range(0, jogador['partidas']):
        try:
            gols.append(int(input(f'O jogador {jogador["nome"]} marcou quantos gols na {g+1}ª partida: ')))
        except:
            continue
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    ficha_jogadores.append(jogador.copy())
    print('-'*40)
    while True:
        exit = str(input('Deseja continuar? [S/N] ')).upper()[0]
        print('-'*40)
        if exit in 'SN':
            break
        print('Valor inválido, digite "S" ou "N".')
    if exit == 'N':
        break
print('='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(ficha_jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Digite o código do jogador: (999 para encerrar) '))
    if busca == 999:
        break
    if busca >= len(ficha_jogadores):
        print(f'ERRO! código {busca} inválido.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {ficha_jogadores[busca]["nome"].upper()}:')
        for i, g in enumerate(ficha_jogadores[busca]['gols']):
            print(f'   No {i+1}° jogo fez {g} gols')
    print('-'*40)
print('>>>> VOLTE SEMPRE! <<<<')
