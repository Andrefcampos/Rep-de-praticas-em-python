'''Programa que ler um ano qualquer e informe se é
ano bissexto ou não'''

import calendar
ano = int(input('Qual ano você quer analisar? '))
print('-=-'*20)
print('Você escolheu o ano {}'.format(ano))
print('-=-'*20)

if calendar.isleap(ano):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))