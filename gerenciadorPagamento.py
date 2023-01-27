'''Programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condições de pagamento:
- a vista dinheiro /  cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x no cartão: 20% de juros'''
valor = float(input('Qual o valor do produto? R$ '))
print('{}-*{}'.format('\33[1;33m', '\33[m')*15)
print('Escolha uma das opções de pagamento:{}1- Dinheiro / Cheque{}2- Cartão à vista{}3- 2x no cartão{}4- 3x no cartão'.format('\n', '\n', '\n', '\n'))
print('{}-*{}'.format('\33[1;33m', '\33[m')*15)
pgmt = int(input('Qual a forma de pagamento pretendida? '))
print('{}-*{}'.format('\33[1;33m', '\33[m')*15)
if pgmt == 1:
    print('Você escolheu pagamento em dinheiro/cheque. O valor de R${:.2f} receberá um desconto de 10%, totalizando R${:.2f}.'.format(valor, valor - (valor*0.1)))
elif pgmt == 2:
    print('Você escolheu pagamento cartão à vista. O valor de R${:.2f} receberá um desconto de 5%,totalizando R${:.2f}.'.format(valor, valor - (valor*0.05)))
elif pgmt == 3:
    print('Você escolheu pagamento em 2x no cartão. O total é R${:.2f}.'.format(valor))
elif pgmt == 4:
    print('Você escolheu pagamento e 3x no cartão. O valor de R${:.2f} receberá um acréscimo de 20% pelo juros da máquina, totalizando R${:.2f}.'.format(valor, valor*1.2))
else:
    print('Opção inválida. Tente novamente com uma das opção sugeridas no menu.')
