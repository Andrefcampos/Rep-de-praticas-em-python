'''Programa que tenha uma função chamada área que mostre:
- terreno retangular (largura e comprimento
- mostrar a área do terreno.'''
def area():
    largura = int(input('Largura: '))
    comprimento = int(input('Comprimento: '))
    tot_area = largura * comprimento
    print(f'> A largura do terreno é de {largura}m')
    print(f'>> O comprimento do terreno é de {comprimento}m')
    print('-'*40)
    print(f'>>> A área do terreno é de {tot_area}m²')


print('='*40)
print(f'{"MEDIÇÃO TERRENO":^40}')
print('='*40)
area()
