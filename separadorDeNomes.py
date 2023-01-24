'''Programa que lê:
- Nome completo de uma pessoa;
- Mostrar o primeiro nome (separadamente);
- Mostrar o último nome (separadamente).
Ex: Ana Maria de Souza
primeiro == Ana
último == Souza'''

nome = str(input('Insira seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))