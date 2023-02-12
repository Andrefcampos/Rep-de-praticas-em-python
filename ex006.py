'''Programa que o usuario digite uma expressão
 qualquer que use parenteses.
 - o aplicativo deverá analisar a expressão passada esta
 com os parenteses abertos e fechados na ordem correta.'''
exp = input('Digite uma frase e coloque parenteses, caso desejar: ')
lista = []
cont_a = 0
cont_f = 0
for i in exp:
    if i == '(':
        cont_a += 1
        lista.append('(')
    if i == ')':
        cont_f += 1
        lista.append(')')
if cont_a == cont_f:
    print('Essa expressão é válida.')
else:
    print('Essa expressão é inválida.')

