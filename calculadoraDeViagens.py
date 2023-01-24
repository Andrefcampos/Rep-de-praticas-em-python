'''Programa que pergunta:
- Distancia de uma viagem em km;
- calcule o preço da passagem (R$0,50 por km ate 200km e
R$0,45 para viagens mais longas)'''
dist = float(input('Qual a distância a ser percorrida na viagem? '))
print('Você está prestes a começar sua viagem de {}Km'.format(dist))

if dist <= 200.0:
    ate200 =dist * 0.50
    print('A distância da viagem é de {:.1f}km e custará R${:.2f}'.format(dist, ate200))
else:
    acima200 = dist * 0.45
    print('A distância da viagem é de {:.1f}km e custará R${:.2f}.'.format(dist, acima200))