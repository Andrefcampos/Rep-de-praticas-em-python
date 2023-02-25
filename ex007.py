'''Programa que tenha:
- a função chamada voto()
- receber como parametro o ano de nascimento de uma pessoa
- retornando um valor literal indicando se a pessoa tem voto
    - negado
    - opcional
    - obrigatório'''
def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if 16 <= idade <= 65:
        if 18 <= idade <= 65:
            return print('OBRIGATÓRIO')
        else:
            return print('OPCIONAL')
    else:
        return print('NEGADO')
anoNasc = int(input('Ano de nascimento: '))
print('>>> O seu voto é: ', end='')
voto(anoNasc)
