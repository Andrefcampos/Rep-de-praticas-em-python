'''Programa que lê o nome e o peso de várias pessoas
- guardar em uma lista
- a) Quantas pessoas foram cadastradas
- b) uma listagem com as pessoas mais pesadas
- c) Uma listagem com as pessoas mais leves.'''
data = []
list = []
mais_pesado = menos_pesado = 0
while True:
    data.append(str(input('Diga um nome: ')).title())
    data.append(float(input('Diga o peso: ')))
    if len(list) == 0:
        mais_pesado = menos_pesado = data[1]
    else:
        if data[1] > mais_pesado:
            mais_pesado = data[1]
        if data[1] < menos_pesado:
            menos_pesado = data[1]
    list.append(data[:])
    data.clear()
    exit = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if exit == 'N':
        break
print('=' * 40)
print(f'Foram cadastradas {len(list)} pessoas.')
print(f'O maior peso foi {mais_pesado}Kg. De ', end='')
for i in list:
    if i[1] == mais_pesado:
        print(f'[{i[0]}]', end='')
print()
print(f'O menor peso foi {menos_pesado}Kg. De ', end='')
for i in list:
    if i[1] == menos_pesado:
        print(f'[{i[0]}]', end='')
print()
print('=' * 40)
