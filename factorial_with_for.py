num = int(input('Digite um número: '))
fatorial = 1
cont = num
for cont in range (num, 0, -1):
    print('{}'.format(cont), end='')
    if cont > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
