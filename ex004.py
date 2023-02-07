'''Programa que lê 4 valores pelo teclado e guarde em uma tupla
- quantas vezes aparece o numero 9
- e em que posição foi digitado o primeiro valor 3
- quais foram os números pares'''
num = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto número: ')))
cont9 = par = 0
print(num)
for i in num:
    if i == 9:
        cont9 += 1
    if i % 2 == 0:
        par += 1
print('==' * 20)
print(f'>> O número 9 apareceu {cont9} vezes.')
print(f'>> Há {par} números pares')
