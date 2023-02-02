'''Programa que mostra Tabuada de vários números de cada vez:
- parar quando informar número negativo'''
while True:
    num = int(input('Qual valor você quer calcular? '))
    if num > 0:
        for i in range (0, 10):
            print(f'{num} x {i} = {num * i}')
    print('--' * 20)
    seguir = str(input('>>> Você quer continuar? [S/N] ')).strip().upper()[0]
    print('--' * 20)
    if seguir == 'N':
        break
print('Tudo bem, volte sempre!')
