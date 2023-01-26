'''Programa que lê o ano de nascimento
- informar de acordo com sua idade se:
 - se ele ainda vai se alistar;
 - se é a hora de se alistar;
 - se já passou (informando quanto tempo passou).'''

from datetime import date
print('Olá!')
print('Você quer saber se está na idade de alistamento?\nSe sim, digite: 1\nSe não, digite: 2')
print('\33[1;33m...\33[m'*20)
resposta = int(input('Digite sua opção: '))
print('\33[1;33m...\33[m'*20)
if resposta == 1:
    print('Muito bem!')
    anoNasc = int(input('Qual o seu ano de nascimento? '))
    print('\33[1;33m...\33[m'*20)
    hoje = date.today()
    if hoje.year - anoNasc == 18:
        print('\33[1;42mVocê tem 18 anos, deve se alistar.\33[m')
    elif hoje.year - anoNasc < 18:
        idade = 18 - (hoje.year - anoNasc)
        print('\33[1;43mFaltam {} anos para realizar o alistamento.\33[m'.format(idade))
    else:
        idade = (hoje.year - anoNasc) - 18
        print('\33[1;41mVocê ultrapassou a idade de alistamento em {} anos. Regularize sua situação.\33[m'.format(idade))
elif resposta == 2:
    print('Tudo bem!\nEsperamos você na proxima vez.')
else:
    print('Opção invalida, tente novamente.')