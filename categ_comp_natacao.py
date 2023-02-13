'''programa leia ano de nascimento de atleta
classifique por categorias:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: Sênior
- acima de 20 anos: Master'''
from datetime import date
anoNasc = int(input('Em que ano você nasceu? '))
print('\33[1;33m|-\33[m'*20)
anoAtual = date.today()
idade = anoAtual.year - anoNasc
print('Você tem {} anos.'.format(idade))
print('\33[1;33m|-\33[m'*20)
if idade > 0 and idade < 100:
    if idade <= 9:
        print('Você está classificado na categoria \33[4mMirim\33[m.')
    elif idade <= 14:
        print('Você está classificado na categoria \33[4mInfantil\33[m.')
    elif idade <= 19:
        print('Você está classificado na categoria \33[4mJunior\33[m.')
    elif idade <= 20:
        print('Você está classificado na categoria \33[4mSênior\33[m.')
    else:
        print('Você está classificado na categoria \33[4mMaster\33[m.')
else:
    print('Idade fora dos padrões possíveis, reinicie o programa.')
