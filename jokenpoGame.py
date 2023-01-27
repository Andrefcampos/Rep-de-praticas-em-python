'''Programa que faça o computador jogar jokenpô com você
- pedra papel tesoura'''
from random import choice
from time import sleep
elementos = ('Pedra', 'Papel', 'Tesoura')
jokenpo = choice(elementos)
print('Vamos jogar JOKENPO?')
print('{}-*{}'.format('\33[1;33m', '\33[m')*20)
print('''Esolha um elemento abaixo:
\33[1;32m[0] Pedra
[1] Papel
[3] Tesoura\33[m''')
print('{}-*{}'.format('\33[1;33m', '\33[m')*20)
you = int(input('Jogue: '))
print('{}-*{}'.format('\33[1;33m', '\33[m')*20)
print('\33[1;32mJO\33[m')
sleep(1)
print('\33[1;32mKEN\33[m')
sleep(1)
print('\33[1;32mPO!!!\33[m')
sleep(1)
if you >= 0 and you < 3:
    if you == 0 and jokenpo == 'Pedra' or you == 1 and jokenpo == 'Papel' or you == 2 and jokenpo == 'Tesoura':
        print('''\33[1;43mDEU EMPATE!!\33[m
        Você escolheu \33[1;43m{}\33[m e o computador escolheu \33[1;43m{}\33[m.'''.format(elementos[you], jokenpo))
    elif you == 0 and jokenpo == 'Tesoura':
        print('''\33[1;42mVOCÊ GANHOU!!\33[m
        Sua escolha foi \33[1;42mPEDRA\33[m e o computador \33[1;41mTESOURA\33[m.''')
    elif you == 1 and jokenpo == 'Pedra':
        print('''\33[1;42mVOCÊ GANHOU!!\33[m
        Sua escolha foi \33[1;42mPAPEL\33[m e o computador \33[1;41mPEDRA\33[m.''')
    elif you == 2 and jokenpo == 'Papel':
        print('''\33[1;42mVOCÊ GANOU!!\33[m
        Sua escolha foi \33[1;42mTESOURA\33[m e o computador \33[1;41mPAPEL\33[m.''')
    else:
        you2 = []
        print('''\33[1;41mVOCÊ PERDEU!!\33[m
        Sua escolha foi \33[1;41m{}\33[m e o computador \33[1;42m{}\33[m.'''.format(elementos[you], jokenpo))
else:
    print('Opção inválida, tente novamente.')
