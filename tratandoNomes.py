'''Programa que lê:
- O nome completo da pessoa;
- O nome com todas as letras maiúsculas;
- Quantas letras ao todo (sem considerar espaços);
- Quantas letra tem o primeiro nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()

print('Nome completo = {}'.format(nome))
print('Maiúscula = {}'.format(nome.upper()))
print('Número de letras ao todo sem espaço = {} letras'.format(len(nome) - nome.count(' ')))
print('Numero de letras primeiro nome = {} letras'.format(nome.find(' ')))
#Outra forma de resolver o ultimo item:
separa = nome.split()
print('O primeiro nome é "{}" e possui {} letras'.format(separa[0], len(separa[0])))
