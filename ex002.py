'''Programa que o usuario crie varios valores numéricos
- guardar em uma lista
- eliminar duplicados
- no final exibir todos os valores únicos em ordem crescente'''
lista = []
while True:
    n = int(input('Diga um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado...')
    else:
        print('Valor já foi adicionado, insira outro...')
    exit = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if exit == 'N':
        break
lista.sort()
print(lista)
