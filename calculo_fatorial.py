'''Programa que tenha:
- função chamada fatorial()
- que tenha dois parametros
    - número a calcular
    - show que será o valor lógico (opcional)
- indicando se será mostrado ou não na tela o processo de calculo fatorial'''
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a operação.
    :return: O valor do Fatorial de um número n.
    """

    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


#Programa principal
num = int(input('Digite um número: '))
print(fatorial(num, True))
help(fatorial)
