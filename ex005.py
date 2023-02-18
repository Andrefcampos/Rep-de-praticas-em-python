'''Programa que leia nome e sexo de várias pessoas
- guardar em um dicionário
- no final mostrar quantas pessoas foram cadastradas
- a média de idade do grupo
- uma lista com todas as mulheres
- uma lista com todas as pessoas com idade acima da média.'''
dados = {}
mulheres = []
maior_media = []
media = 0
total_idade = 0
while True:
    nome = str(input('Nome: ')).index()
    sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    idade = int(input('Idade: '))
    exit = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if exit == 'N':
        break
print(dados)