'''Programa que lê:
- O nome de uma pessoa;
- Se há "SILVA" no nome. '''

nome = str(input('Insira seu nome completo: ')).strip()

print('Seu nome possui "SILVA"?\nR: {}'.format('SILVA' in nome.upper()))