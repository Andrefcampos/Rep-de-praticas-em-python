'''Programa que leia vários números inteiros pelo teclado:
- parar quando digitar 999;
- somar quantos números foram digitados
- somar os valores digitados
- mostrar as somas em tela'''
soma = cont = num = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('--' * 20)
print(f'A soma dos {cont} valores é {soma}.')
