'''Módulo chamado moedas.py que tenha as funções incorporadas:
- aumentar()
- diminuir()
- dobro()
- metade()
 -> Criar programa que utilize essas funções importando esse módulo.'''


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res


def aumentar(preço):
    res = preço * 1.1
    return res


def diminuir(preço):
    res = preço / 1.1
    return res
