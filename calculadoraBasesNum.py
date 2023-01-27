'''Programa que leia numero inteiro qualquer
- pedir pro usuario escolher a base de conversão
- 1 para binario
- 2 para octal
- 3 para hexadecimal'''
print('Olá! Seja bem vindo ao conversor de bases numéricas.')
print('\33[1;33m--\33[m'*20)
num = int(input('Digite um número inteiro: '))
print('\33[1;33m--\33[m'*20)
print('Escolha a base de conversão para seu número:\n\33[1;31m1- Binário\33[m\n\33[1;32m2- Octal\33[m\n\33[1;33m3- Hexadecimal\33[m')
escolha = int(input('Digite um número: '))
print('\33[1;33m--\33[m'*20)
if escolha == 1:
    print('Você escolheu \33[1;31m{}\33[m a conversão para \33[1;31mBinário\33[m e o resultado foi \33[1;31m{}\33[m'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('Você escolheu \33[1;32m{}\33[m a conversão para \33[1;32mOctal\33[m e o resultado foi \33[1;32m{}\33[m'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('Você escolheu \33[1;33m{}\33[m a conversão para \33[1;33mHexadecimal\33[m e o resultado foi \33[1;33m{}\33[m'.format(num, hex(num)[2:]))
else:
    print('Este valor não é válido, tente novamente.')
