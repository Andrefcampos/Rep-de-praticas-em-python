''' Progama que leia numero "n" inteiro
- mostrar na tela os "n" primeiros elementos de uma
sequencia de fibonacci.
ex: 0→ 1→ 1→ 2→ 3→ 5→ 8'''
print('~'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('~'*20)
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{} → {}'.format(t1, t2), end='')
while cont <= num:
    t3 = t1 + t2
    print(' → {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM!')
print('~'*20)