'''Programa que lê:
- Nome da sua cidade;
- Se começa ou não com o nome "SANTO".'''

cidNasc = str(input('Em qual cidade você nasceu? ')).strip()

print('Você nasceu em {}'.format(cidNasc.title()))
print('O nome da cidade começa com a palavra santo? {}'.format(cidNasc[:5].upper() == 'SANTO'))