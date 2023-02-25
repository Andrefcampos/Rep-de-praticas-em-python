''' Programa que contenha função:
- ficha() que recebe dois parametros opcionais
    - nome
    - gols
- O programa deverá ser capaz de mostrar a ficha do jogador
mesmo que algum dado não tenha sido informado corretamente.'''
def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
try:
    g = int(input(f'Quantos gols o jogdor {n} fez no campeonato? '))
except:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
