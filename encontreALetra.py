'''Programa que lê:
- Frase pelo teclado;
- Quantas vezes aparece a letra "A";
- Em qual posição ela aparece a primeira vez;
- Em qual posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A última posição da letra "A" é a posição {}'.format(frase.rfind('A')+1))
