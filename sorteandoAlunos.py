#Sortear 4 alunos para apagar o quadro
#Ler o nome deles e escrever o nome do escolhido

from random import choice

aluno1 = str(input('Diga o nome do aluno 1: '))
aluno2 = str(input('Diga o nome do aluno 2: '))
aluno3 = str(input('Diga o nome do aluno 3: '))
aluno4 = str(input('Diga o nome do aluno 4: '))
list = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(list)

print('O professor irá escolher entre os alunos {} para apagar o quadro. \nO escolhido foi {}.'.format(list, escolhido))
