'''Programa que leia o nome, ano de nascimento, ctps
- cadastre-os (com idade) em um dicionário
- ctps diferente de 0 o dicionario receberá também o ano da contratação e o salario
- calcular e acrescentar, alem da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('CTPS: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Data primeira contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('=' * 30)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')