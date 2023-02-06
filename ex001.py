'''Programa que tenha uma tupla
- preencher com uma contagem pore extenso (0, 20)
- Ele deverá ler um numero pelo teclado entre 0 e 20 e mostra-lo por extenso'''
print('==' * 20)
print(f'{"LEITOR DE NÚMEROS POR EXTENSO":^40}')
print('==' * 20)
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Diga um número de 0 a 20: '))
    exit = ''
    if 0 <= num <= 20:
        print(f'O número que você escolheu foi: {numeros[num]}')
        print('--' * 20)
        exit = str(input('>>> Você deseja continuar? [S/N] ')).strip().upper()[0]
        print('--' * 20)
        if exit == 'S':
            continue
        else:
            break
    else:
        print('O número digitado está fora do intervalo, tente novamente. ', end='')
print('Fim!')
