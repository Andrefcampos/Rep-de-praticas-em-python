'''Programa que le 3 retas e informa se forma triangulo
- dizer se é equilatero, isoceles ou escaleno'''
from math import hypot
print('\33[1;33m-=-\33[m'*20)
print('\33[1;34mANALISADOR DE TRIÂNGULOS\33[m')
print('\33[1;33m-=-\33[m'*20)
print('Vamos ver se 3 retas formam um triângulo.')
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
if reta1 + reta2 < reta3 or reta1 + reta3 < reta2 or reta2 + reta3 < reta1:
    print("Esses valores {}não{} podem formar um triângulo.".format('\33[41m', '\33[m'))
else:
    print('Esses valores podem formar um triângulo.')
    if reta1 == reta2 and reta2 == reta3 and reta1 == reta3:
        print('{}Triângulo equilátero{}'.format('\33[1;44m', '\33[m'))
    elif reta1 == hypot(reta2, reta3) or reta2 == hypot(reta1, reta3) or reta3 == hypot(reta1, reta2):
        print('{}Triângulo retângulo{}'.format('\33[1;42m', '\33[m'))
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('{}Triângulo isóceles{}'.format('\33[1;43m', '\33[m'))
    else:
        print('fim')
