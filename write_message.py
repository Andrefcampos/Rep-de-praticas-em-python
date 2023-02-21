'''Programa que tenha uma função chamada:
- escreva()
- receber texto qualquer como parametro
- mostrar uma menságem com tamanho adaptável.'''
def escreva(txt):
    print('='*(len(txt)+20))
    print(f'{txt:^{len(txt) + 20}}')
    print('=' * (len(txt) + 20))


txt = str(input('Deixe sua mensagem: ')).title()
escreva(txt)
