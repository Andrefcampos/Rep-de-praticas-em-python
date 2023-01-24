''' Programa que lê:
- Número de 0 a 9999
- Mostrar em tela cada um separado
(Unidade, dezena, centena, milhar)'''

num = int(input('Digite um número de 0 a 9999: '))

print('O número é: {}\nMilhar: {} \nCentena: {}\nDezena: {}\nUnidade: {}'.format(num, num//1000%10, num//100%10, num//10%10, num//1%10))
