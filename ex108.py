'''Adaptar o código do desafio 107 criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.'''
import moedas
p = float(input('Digite um valor: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10%, temos R${moedas.moeda(moedas.aumentar(p, 10))}')
