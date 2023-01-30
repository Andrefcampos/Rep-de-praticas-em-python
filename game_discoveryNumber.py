''' Melhorar o jogo do desafio 028:
- computador pensar um número entre 0 e 10;
- o jogador irá tentar até acertar'''
from random import randint
print('Vamos jogar!')
print('Escolha um número de 0 a 10 e tente acertar qual eu pensei.')
pc = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    num = int(input('Insira seu palpite: '))
    palpites += 1
    if num == pc:
        acertou = True
        print('Você acertou, o seu palpite foi {} e o que pensei foi {}.'.format(num, pc))
        print('Você realizou um total de {} tentativas para encontrar o número que eu pensei.'.format(palpites))
    else:
        if num < pc:
            print('Eu pensei em um número maior, tente novamente!')
        else:
            print('Pensei em um número menor, tente novamente!')
