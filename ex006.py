'''Programa que tenha uma tupla com várias palavras (não usar acentos)
 - mostrar pra cada palavra as suas vogais'''
palavra = ('casa', 'viagem', 'dormir', 'programar', 'renascer', 'viver')
for p in palavra:
    print(f'\nA palavra {p.upper()} tem ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')