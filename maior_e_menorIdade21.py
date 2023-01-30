'''Programa que lê o ano de nascimento de 7 pessoas
- no final informar quantas ja atingiram a maior idade e quantas não atingiram.'''
from datetime import date
anoAtual = date.today().year
maior_idade = 0
menor_idade = 0
for i in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    if anoAtual - ano >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
print('Tivemos {} pessoas que atingiram a maior idade.'.format(maior_idade))
print('Tivemos {} pessoas que ainda não atingiram a maior idade.'.format(menor_idade))

