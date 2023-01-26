'''Programa que lê duas notas de um aluno
- calcule a média
- mostra a mensagem final se
 - aprovado >=7.0;
 - reprovado <5.0;
 - recuperação 5.0>=<6.9.'''
nota1 = float(input('Diga sua primeira nota: '))
nota2 = float(input('Diga sua segunda nota: '))
media = (nota1 + nota2) / 2
if nota1 >= 0.0 and nota1 <= 10.0 and nota2 >= 0.0 and nota2 <= 10.0:
    if media >= 7.0:
        print('Aprovado com a média {:.1f}.'.format(media))
    elif media < 5.0:
        print('Reprovdo com a média {:.1f}.'.format(media))
    else:
        print('Você está de recuperação com a média {:.1f}.'.format(media))
else:
    print('ALguma nota está errada, revise e reinicie o programa')
