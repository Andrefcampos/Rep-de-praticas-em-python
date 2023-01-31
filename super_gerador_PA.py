'''
Melhorar o desafio 61
- ao inves de mostrar 10, perguntar se qual termo quer mostrar.
'''
print('SUPER GERADOR DE PA')
print('-*'*25)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão de uma PA: '))
termo = pt
cont = 1
mais = 10
total = 0
while mais !=0:
    total += mais
    while cont <= total:
        print('{}→ '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA. ')
    mais = int(input('Digite até qual termo você deseja saber o valor: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
