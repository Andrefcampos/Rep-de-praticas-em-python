'''Programa que tenha uma função chamada área que mostre:
- terreno retangular (largura e comprimento
- mostrar a área do terreno.'''
def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}m² x {comp}m² é {a}m²')


print('='*40)
print(f'{"MEDIÇÃO TERRENO":^40}')
print('='*40)
l = float(input('Largura (m) = '))
c = float(input('Comprimento (m) = '))
area(l, c)
