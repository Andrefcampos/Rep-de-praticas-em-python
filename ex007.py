'''Programa que tenha:
- a função chamada voto()
- receber como parametro o ano de nascimento de uma pessoa
- retornando um valor literal indicando se a pessoa tem voto
    - negado
    - opcional
    - obrigatório'''
from datetime import date
def voto(ano):
    hoje = date.today().year
    idade = hoje - ano
    if idade >= 16:
        if idade >= 18:
            return print('OBRIGATÓRIO')
        else:
            return print('OPCIONAL')
    else:
        return print('NEGADO')
anoNasc = int(input('Ano de nascimento: '))
print('>>> O seu voto é: ', end='')
voto(anoNasc)
