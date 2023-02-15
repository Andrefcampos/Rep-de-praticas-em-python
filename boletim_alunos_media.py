'''Programa que leia o nome e duas notas de vários alunos
- guardar tudo em uma lista composta
- no final mostrar o boletim contendo média de cada um
- permitir que o usuario possa mostrar a nota de cada um individualmente'''
print('='*30)
print(f'{"BOLETIM ALUNOS":^30}')
print('='*30)
dados = []
while True:
    aluno = str(input('Digite o nome do aluno: ')).title()
    nota1 = float(input('Digite a 1ª nota do aluno: '))
    nota2 = float(input('Digite a 2ª nota do aluno: '))
    media = (nota1 + nota2) / 2
    dados.append([aluno, [nota1, nota2], media])
    exit = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if exit == 'N':
        break
print('='*30)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
print('-'*30)
while True:
    opc = int(input('Digite o número do aluno que deseja ver a nota: '))
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
        print('-'*30)
    else:
        print('Você digitou um valor diferente da quantidade de alunos cadastrados. finalizando o programa...')
        break
print('>>>>> VOLTE SEMPRE! <<<<<')
