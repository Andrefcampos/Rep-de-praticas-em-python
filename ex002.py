'''Receber os valores dos catetos e calcular
a hipotensa de um triangulo retângulo e imprimir na tela
o resultado
'''
from math import hypot

cat_oposto = float(input('Informe o comprimento do cateto oposto: '))
cat_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)
print('A hipotenusa é {:.2f}'.format(hipotenusa))