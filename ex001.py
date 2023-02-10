'''Programa que leia 5 valores númericos
- armazenar numa lista
- mostrar o maior e o menor
- mostrar a posição de cada um'''
valores = []
min = max = 0
for v in range(0, 5):
    valores.append(int(input('Diga o valor: ')))
    if v == 0:
        min = max = valores[v]
    else:
        if valores[v] > max:
            max = valores[v]
        if valores[v] < min:
            min = valores[v]
print(valores)
print(f'O maior valor foi {max} na posição ', end='')
for pos, i in enumerate(valores):
    if i == max:
        print(f'{pos}...', end='')
print(f'O menor valor foi {min} na posição ', end='')
for pos, i in enumerate(valores):
    if i == min:
        print(f'{pos}...', end='')