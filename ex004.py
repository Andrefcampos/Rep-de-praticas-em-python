'''Refazer o exercicio 009 mostrando a tabuada de um número que o usuário escolher:
- utilizar o laço de repetição "for"'''
print('TABUADA DE MULTIPLICAÇÃO')
print('{}-*{}'.format('\33[1;32m', '\33[m')*15)
num = int(input('Digite um número: '))
for i in range (1, 11):
    print('{} x {:2} = {}'.format(num, i, num*i))
print('FIM!')