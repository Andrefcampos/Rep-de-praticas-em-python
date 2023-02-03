'''Programa que simula um caixa eletrônico:
- informar valor para saque;
- disponibilzar apenas notas de 50, 20, 10, 1;
- contabilizar quantas notas de cada valor foi utilizado.'''

print('==' * 20)
print('{:-^40}'.format('BANCO MALCON X'))
print('==' * 20)
valor_saque = int(input('Valor do saque: R$ '))
cedulas = [50, 20, 10, 1]
for i in cedulas:
    total_cedulas = valor_saque // i
    valor_saque %= i
    if total_cedulas > 0:
        print(f'>> foi utilizado {total_cedulas} cédulas de R$ {i:.2f}')
print('Para efetuar o seu saque.')
print('==' * 20)
print(' >>> O BANCO MALCON X agradece a sua preferência.')
print('Adoramos atender você. Volte sempre!')
print('==' * 20)
