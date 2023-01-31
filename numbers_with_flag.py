''' Programa que leia varios números inteiros pelo teclado
- programa irá parar quando chegar a 999
- no final mostrar quantos números foram digitados e qual a soma entre eles
(desconsiderando o flag "999")'''
soma = cont = 0
num = int(input('Digite um número: '))
while num != 999:
        cont += 1
        soma += num
        num = int(input('Digite um número: '))
print('Foram digitados {} números e a soma deles seu {}.'.format(cont, soma))
