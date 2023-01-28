'''Programa que calcule a soma entre todos os números impares que são multiplos de três
- que se encontram no intervalo de 1 a 500.'''
soma = 0
cont = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print('A soma dos {} valores solicitados é {}'.format(cont, soma))

