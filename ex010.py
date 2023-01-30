'''Programa que leia o peso de 5 pessoas:
- no final mostrar qual o peso maior e o peso menor.'''

mais_pesados = 0
menos_pesados = 0
for i in range(1,6):
    peso = float(input('Diga o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        mais_pesados = peso
        menos_pesados = peso
    else:
        if peso > mais_pesados:
            mais_pesados = peso
        if peso < menos_pesados:
            menos_pesados = peso
print('-*'*20)
print('O maior peso lido foi de \33[1;41m{}kg\33[m.'.format(mais_pesados))
print('O menor peso lido foi de \33[1;42m{}kg\33[m.'.format(menos_pesados))