'''Programa em que o usuario insira 5 valores
- cadastrar em lista
- ja cadastrar na posição crescente (não usar função sort())
- mostrar no final a lista ordenada em tela'''
lista = []
for i in range(0, 5):
    v = int(input('Diga um número: '))
    if i == 0 or v > lista[-1]:
        lista.append(v)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}.')
