'''Programa que cria uma matriz 3x3
- preencher com os valores lidos pelo teclado
- mostrar a matriz na tela com a formação correta'''
list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('=' * 40)
print(f'{"MATRIZ 3X3":^40}')
print('=' * 40)
for i in range (0, 3):
    for c in range(0, 3):
        list[i][c] = int(input(f'Digite um valor [{i}, {c}]: '))
print('=' * 40)
for i in range (0, 3):
    for c in range(0, 3):
        print(f'[{list[i][c]:^5}]', end='')
    print()
    
