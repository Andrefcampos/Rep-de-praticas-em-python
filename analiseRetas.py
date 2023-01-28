'''Programa que leia o comprimento de 3 retas e
se pode ou não formar um triangulo'''
print('\33[1;33m-=-\33[m'*20)
print('\33[1;34mANALISADOR DE TRIÂNGULOS\33[m')
print('\33[1;33m-=-\33[m'*20)
print('Vamos ver se 3 retas formam um triângulo.')
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
if reta1 + reta2 < reta3 or reta1 + reta3 < reta2 or reta2 + reta3 < reta1:
    print("Essas retas {}não{} podem formar um triângulo.".format('\33[31m', '\33[m'))
else:
    print('essas retas podem formar um triângulo.')
