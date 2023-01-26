'''Programa que lê o peso e altura e calcule o IMC
- abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida'''
from math import pow
print('Olá!{}Vamos calcular o seu IMC'.format('\n'))
print('{}-*{}'.format('\33[1;33m', '\33[m')*15)
alt = float(input('Qual a sua altura em metros? '))
peso = float(input('Qual o seu peso em quilos? '))
imc = peso / pow(alt, 2)
print('Seu IMC é: {:.1f}'.format(imc))
print('{}-*{}'.format('\33[1;33m', '\33[m')*15)
if imc < 18.5:
    print('{}Você está abaixo do peso ideal{}'.format('\33[1;43m', '\33[m'))
elif imc > 18.5 and imc < 25.0:
    print('{}Você está com o peso ideal{}'.format('\33[1;42m', '\33[m'))
elif imc >= 25.0 and imc <= 30.0:
    print('{}Você está com sobrepeso{}'.format('\33[1;41m', '\33[m'))
elif imc >= 30.0 and imc <= 40.0:
    print('{}Você está com obesidade{}'.format('\33[1;41m', '\33[m'))
else:
    print('{}Você está com obesidade mórbida{}'.format('\33[1;41m', '\33[m'))
