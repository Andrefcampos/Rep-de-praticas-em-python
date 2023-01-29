'''programa que leia 6 números inteiros
- mostrar a soma apenas dos pares
- se o valor digitado for impar, desconsiderar.'''
print('Digite 6 números e o programa irá identificar os pares e somar. Os impares serão descartados.')
soma = 0
cont = 0
for i in range (1,7):
    num = int(input('Digite o {} número: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
