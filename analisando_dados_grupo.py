'''Programa que lê a idade e o sexo de várias pessoas:
- Perguntar se o usuário quer ou não continuar
- mostrar quantas pessoas tem 18 anos;
- quantos homens foram cadastrasdos;
- quantas mulheres tem menos de 20 anos.'''
while True:
    idade = int(input('Diga sua idade: '))
    qnt18 = qntH = qntM = 0
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Diga seu sexo: [F/M] ')).strip().upper()[0]
        print('--' * 20)
    if sexo == 'M':
        qntH += 1
    if idade >= 18:
        qnt18 += 1
    if sexo == 'F':
        if idade < 20:
            qntM += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('>>>> Você deseja continuar? [S/N] ')).strip().upper()[0]
        print('--' * 20)
    if resposta == 'N':
        break
print(f'Há {qntH} homens cadastrados.')
print(f'Há {qnt18} com 18 anos ou mais.')
print(f'Há {qntM} mulheres com menos de 20 anos.')
print('--' * 20)
print('FIM')
