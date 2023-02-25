'''Mini sistema que utilize o interactive Help do python
- O usuario vai digitar o comando e o manual vai aparecer
- quando o usuario digitar "FIM" o programa encerrará.
obs: use cores'''
def ajuda(txt):
    msg = f"Acessando o manual do comando '{txt}'"
    print('\33[1;44m=' * (len(msg)))
    print(f'{msg:^{len(msg)}}')
    print('=' * (len(msg)))
    print('\33[m\33[7m')
    help(txt)
    print('\33[m')


while True:
    psystem = 'SISTEMA DE AJUDA PyHELP'
    print('\33[42m=' * (len(psystem) + 6))
    print(f'{psystem:^{(len(psystem) + 6)}}')
    print('=' * (len(psystem) + 6))
    print('\33[m')
    comando = str(input('Função ou Biblioteca > ')).upper()
    if comando != 'FIM':
        ajuda(comando.lower())
    else:
        break
end = 'ATÉ LOGO!'
print('\33[41m=' * (len(end) + 6))
print(f'{end:^{(len(end) + 6)}}')
print('=' * (len(end) + 6))
print('\33[m')
