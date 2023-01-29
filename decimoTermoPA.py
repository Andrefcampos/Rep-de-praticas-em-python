'''programa que leia o primeiro termo e a razão de uma P.A
- no final mostrar os 10 primeiros termos dessa progressão.'''
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dt = pt + r * (10 - 1)
for i in range(pt, dt + r, r):
    print('{}'.format(i), end='→ ')
print('FIM!!')
