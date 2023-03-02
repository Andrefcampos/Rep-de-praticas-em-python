import moedas
p = float(input('Digite um valor: R$ '))
print(f'A metade de R${p} é R${moedas.metade(p):.2f}')
print(f'O dobro de R${p} é R${moedas.dobro(p):.2f}')
print(f'Aumentando 10%, temos R${moedas.aumentar(p):.2f}')