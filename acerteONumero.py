''' Faça o computador pensar em um número inteiro
entre 0 e 5
peça pro usuário descobrir qual o número escolhido pelo computador
o programa deverá imprimir na tela a mensagem de acerto ou erro.
'''
import random
num = random.randint(0,5)
print('-=-'*25)
print('O computador está pensando em um número de 0 a 5, será se você acerta?')
print('-=-'*25)
palpite = int(input('Dê o seu palpite: '))
print('O seu palpite foi {}'.format(palpite))
print('O número pensado pelo computador foi {}'.format(num))
print('PARABÉNS!\nVocê acertou.' if palpite == num else 'QUE PENA!\nVocê errou.\nEu pensei no número {} e não no número {}.'.format(num, palpite))