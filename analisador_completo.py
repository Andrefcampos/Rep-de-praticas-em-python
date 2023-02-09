'''Programa que lê de 4 pessoas:
-nome
- idade
- sexo
mostrar:
- média de idade
- idade do homem mais velho
- quantas mulheres tem menos de 20 anos.
'''
soma_idade = media_idade = maior_idade_homem = soma_mulher = 0
nome_mais_velho = ''
for i in range (1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        soma_mulher += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {:.1} anos.'.format(media_idade))
print('A idade do homem mais velho é {} anos e ele se chama {}.'.format(maior_idade_homem, nome_mais_velho.title()))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(soma_mulher))
