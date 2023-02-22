'''Programa que tenha uma função chamada maior() que receba vários parametros com valores inteiros:
- analisar todos os valores e dizer qual deles é o maior.'''
def maior():
    maior = 0
    for i in range(0, numeros):
        if i == 0:
            maior = i = 0
            print(f'O maior valor foi {maior}.')
        elif maior > i:
            maior = i
            print(f'O maior valor foi {maior}.')


numeros = []
while True:
    numeros.append(int(input('Digite valores: ')))
    exit = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if exit == 'N':
        print('Obrigado!')
        break
print(f'Os valores foram: {numeros} e o maior valor foi {maior()}')
