'''Programa que vai ler vários numeros
- quantos numeros foram digitados
- lista de valores decrescentes
- se o 5 foi digitado e se está ou não na lista'''
lista = []
pergunta = ''
while True:
    valor = lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não está na lista.')
lista.sort(reverse=True)
print(f'A lista criada foi: {lista}')