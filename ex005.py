'''Programa que lê o nome e o preço de vários produtos:
- qual o total gasto;
- quantos produtos custaram mais de R$1000
- mostrar o produto mais barato
- perguntar sempre se quer ou não continuar'''
total = menor = cont = more1000 = 0
cheap = ' '
while True:
    product = str(input('Nome do produto: '))
    price = float(input('Preço do produto: R$ '))
    print('---' * 20)
    total += price
    cont += 1
    if price >= 1000.0:
        more1000 += 1
    if cont == 1 or price < menor:
        menor = price
        cheap = product
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('>>> Deseja continuar? [S/N] ')).strip().upper()[0]
        print('---' * 20)
    if pergunta == 'N':
        break
print(f'>> O total foi R$ {total:.2f}')
print(f'>> Houve {more1000} produtos com preço acima de R$ 1.000,00.')
print(f'>> O produto mais barato foi {cheap} que saiu no valor de R$ {menor:.2f}')
print('>>>>>>>> Fim!!')
