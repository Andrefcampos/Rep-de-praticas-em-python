#Digitar um número e o programa entregará a sua parte inteira
'''Foi utilizado módulo apenas para praticar, porém dá pra usar apenas "int()"'''

from math import trunc

num = float(input('Digite um número: '))

print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))
