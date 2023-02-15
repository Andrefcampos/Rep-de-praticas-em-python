'''Aprimorar o desafio anterior
- mostrando a soma dos valores pares
- a soma dos valores da terceira coluna
- o maior valor da segunda linha'''
list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        list[linha][coluna] = int(input(f'Preencha o valor [{linha}, {coluna}]: '))
print('=' * 30)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{list[linha][coluna]:^5}]', end='')
        if list[linha][coluna] % 2 == 0:
            spar += list[linha][coluna]
    print()
print('=' * 30)
print(f'>>> A soma dos valores pares é {spar}.')
for linha in range (0, 3):
    scol += list[linha][2]
print(f'>>> A soma da terceira coluna é {scol}.')
for coluna in range (0, 3):
    if list[1][coluna] == 0:
        list[1][coluna] = maior = 0
    elif list[1][coluna] > maior:
        maior = list[1][coluna]
print(f'>>> O maior número da segunda coluna é igual a {maior}.')
