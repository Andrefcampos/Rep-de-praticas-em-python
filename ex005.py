'''Programa que le varios números
- adicionar em uma lista
- criar duas listas que vão contar 1 par e outra impar
- mostrar o conteudo das três geradas'''
lista = []
listaPar = []
listaImpar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num != 0:
        if num % 2 == 0:
            listaPar.append(num)
            print(f'>>> O número {num} é par, foi adcionado à lista de números pares...')
        else:
            listaImpar.append(num)
            print(f'>>> O número {num} é impar, foi adicionado à lista de números ímpares...')
        pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
lista.sort()
print('=' * 40)
print(f'Os números foram: {lista}')
print(f'Destes números, os pares foram: {listaPar}')
print(f'Os ímpares foram: {listaImpar}')
