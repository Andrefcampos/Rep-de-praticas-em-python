'''Prorgrama que leia salário do empregado e dê aumento
- para salários superior a R$1200 (aumento de 10%)
- salarios inferiores ou iguais a R$1200 (aumento de 15%)'''
salario = float(input('Qual o salário a ser aumentado? '))
if salario > 1200.0:
    aumento = salario * 1.10
    print('O aumento será de 10% que resultará no total de R${:.2f}'.format(aumento))
else:
    aumento = salario * 1.15
    print('O aumento será de 15% que resultará no total de R${:.2f}'.format(aumento))