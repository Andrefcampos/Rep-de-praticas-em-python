'''Programa que vai gerar 5 numeros aleatorios e colocar me uma tupla
- mostrar a listagem de números gerados
- indicar o menor e o maior valores da tupla'''
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: {num}.')
for n in num:
    print(f'{n} ', end='')
print(f'\n-> O maior valor gerado foi: {max(num)}.')
print(f'-> O menor valor gerado foi: {min(num)}.')