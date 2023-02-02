''' Programa que leia varios números inteiros pelo teclado
- programa irá parar quando chegar a 999
- no final mostrar quantos números foram digitados e qual a soma entre eles
(desconsiderando o flag "999")'''
soma = cont = num = 0
while True:
        num = int(input('Digite um número: '))
        if num == 999:
                break
        cont += 1
        soma += num 
print('Foram digitados {} números e a soma deles seu {}.'.format(cont, soma))
