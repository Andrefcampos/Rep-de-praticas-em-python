'''Programa que leia o nome e a média de um aluno
- guardar também a situação em um dicionário
- no final mostrar o conteúdo da estrutura na tela.'''
aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input('Digite a média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 4 < aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'>>> {k} é igual a {v}.')
    
