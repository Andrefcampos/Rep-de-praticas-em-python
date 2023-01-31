''' Programa que leia 2 valores e mostre um menu
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Deverá realizar a operação em cada caso
'''
from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
option = 0
while option != 5:
    print('''Qual operação deseja realizar com esse número?
[1] Somar
[2] Multiplicar
[3] Informar o maior
[4] Novos números
[5] Sair do programa''')
    option = int(input('>>>>>> Qual a sua opção? '))
    if option == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif option == 2:
        print('{} x {} = {}}'.format(num1, num2, num1 * num2))
    elif option == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 < num2:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('Os números são iguais.')
    elif option == 4:
        print('Informe os valores novamente:')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    print('-.' * 10)
    sleep(2)
print('Fim do programa.')
