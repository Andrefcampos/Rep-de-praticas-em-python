'''Programa que leia nome e sexo de várias pessoas
- guardar em um dicionário
- no final mostrar quantas pessoas foram cadastradas
- a média de idade do grupo
- uma lista com todas as mulheres
- uma lista com todas as pessoas com idade acima da média.'''
dados = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Valor inválido, digite "F" ou "M"  para prosseguir.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        exit = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if exit in 'SN':
            break
        print('Valor inválido digite "S" ou "N".')
    if exit == 'N':
        break
print('='*30)
print(dados)
print(f'A - Ao todo temos {len(dados)} pessoas cadastradas.')
media = soma / len(dados)
print(f'B - A média de idade das pessoas cadastradas é {media:.2f} anos')
print(f'C - As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D - Lista de pessoas com idadee acima da média: ', end='')
for p in dados:
    if p['idade'] > media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
            print()
print('>>>>>>> FIM <<<<<<<')
