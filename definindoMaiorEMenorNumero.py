'''Programa que leia 3 números e
mostre qual o maior e qual o menor'''
print('-=-'*20)
print('Olá, o programa irá analisar qual o maior e menor número.')
print('-=-'*20)
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a < b and a < c:
    print('O menor número é {}'.format(a))
if b < a and b < c:
    print('O menor número é {}'.format(b))
if c < a and c < b:
    print('O menor número é {}'.format(c))
if a > b and a > c:
    print('O maior número é {}'.format(a))
if b > a and b > c:
    print('O maior número é {}'.format(b))
if c > a and c > b:
    print('O maior número é {}'.format(c))