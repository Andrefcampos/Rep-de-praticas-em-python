'''Escrever a velocidade do carro
- se passar de 80km/h = multado
- se for inferior a 80km/h não foi multado
- valor da multa (R$7,00 por cada km acima da velocidade limite'''
vel = float(input('Qual a velocidade atingida? '))
print('Tenha um bom dia e dirija com segurança!' if vel <= 80.0 else 'VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE PERMITIDA. REDUZA!')
print('-=-'*25)
print('Sua velocidade foi {:.2f}km/h'.format(vel))
print('-=-'*25)
if vel < 80.0:
    print('Sua velocidade foi abaixo do limite de velocidade.\nVocê não foi multado!')
else:
    multa = (vel - 80.0) * 7.0
    print('Você atingiu a velocidade de {:.2f}km/h\nO valor da sua multa é de R$ {:.2f}'.format(vel, multa))