'''Programa pro usuario escrever 7 valores numéricos
- cadastrar em uma lista
- manter separados os valores pares dos impares
- final mostrar valores pares e impares em ordem crescente.'''
list = [[], []]
valor = 0
for i in range (1,8):
    valor = int(input('Digite o valor: '))
    if valor % 2 == 0:
        list[0].append(valor)
    else:
        list[1].append(valor)
print('-' * 40)
list[0].sort()
print(f'Os valores pares foram: {list[0]}')
list[1].sort()
print(f'Os valores ímpares foram: {list[1]}')
print(f'todos os valores foram: {list}')