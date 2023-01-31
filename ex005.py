''' Refazer o desafio 051
- o primeiro termo
- ler a razão
- ler ler os 10 primeiros termos
* usar estrutura while'''
print('GERADOR DE PA')
print('-*'*25)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = pt
while cont <= 10:
    print('{}→ '.format(termo), end='')
    termo += r
    cont += 1
print('FIM!')