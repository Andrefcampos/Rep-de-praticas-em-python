''' Programa que leia o sexo de uma pessoa
- somente aceits 'M' ou 'F'
'''
sexo = str(input('Diga o seu sexo: [F/M] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite seu sexo: [F/M] ')).strip().upper()[0]
if sexo == 'F':
    print('O seu sexo é Femino.')
if sexo == 'M':
    print('O seu sexo é Masculino.')
print('FIM!')
