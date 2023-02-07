'''Criar tupla com a tebala dos 20 times primeiros colocados da tabela do brasileirão
- os 5 primeiros colocados
- os 4 ultimos colocados
- uma lista com os times em ordem alfabetica (sort())
- Em que posição da tabela está o time chapecoense.'''
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico PR', 'Atlético MG',
         'Fortaleza', 'São Paulo', 'América MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará SC', 'Atlético GO', 'Avaí', 'Juventude')
print('>>> Os 5 primeiros times da tabela do Brasileirão 2022 são: ')
for pos, i in enumerate(times[0:5]):
    print(f'{pos + 1}ª {i}')
print('>>> Os 4 últimos times da tabela do Brasileirão são:')
for pos, i in enumerate(times[16:20]):
    print(f'{pos + 17}ª {i}')
print(f'>>> O Flamengo está na {times.index("Flamengo") + 1}ª posição')
print('>>> Em ordem alfabética os times ficam organizados da seguinte forma:')
print(sorted(times))
