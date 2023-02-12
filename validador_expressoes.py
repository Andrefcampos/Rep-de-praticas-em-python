'''Programa que o usuario digite uma expressão
 qualquer que use parenteses.
 - o aplicativo deverá analisar a expressão passada esta
 com os parenteses abertos e fechados na ordem correta.'''
expressao = str(input('Digite uma epressão matamática: '))
lista = []
for i in expressao:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
