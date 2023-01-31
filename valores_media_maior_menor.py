'''Programa que leia varios númeors inteiros pelo teclado
- final mostrar média de todos os valores
- maior e menor número
- perguntar sempre se quer continuar ou não a digitar valores.'''
pergunta = 'S'
num = cont = media = soma = maior = menor = 0
while pergunta in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print('Você digitou {} números e a média deles é {}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
