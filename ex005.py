'''Programa que tenha uma tupla unica
com nomes de produtos e seus respectivos preços
- mostrar listagem de preços organizando os dados em forma tabular.'''
listagem = ('Arroz 5Kg', 21.7,
            'Feijão 1Kg', 8.9,
            'Peixe 3Kg', 35.5,
            'Carne 5Kg', 250.6)
total = 0
print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('='*40)
print(f'{"ITENS":<30}', end='')
print(f'{"PREÇO":>10}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
        total += listagem[pos]
print('='*40)
print(f'{"TOTAL = ":.<30}', end='')
if pos % 2 != 0:
    print(f'R$ {total:7.2f}')