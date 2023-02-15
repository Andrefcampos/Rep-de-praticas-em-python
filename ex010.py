'''Aprimorar o desafio anterior
- mostrando a soma dos valores pares
- a soma dos valores da terceira coluna
- o maior valor da segunda linha'''
list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3):
    for coluna in range (0, 3):
        list[linha][coluna] = int(input(f'Preencha o valor [{linha}, {coluna}]: '))
print()
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[{list[linha][coluna]:^5}]', end='')
    print()