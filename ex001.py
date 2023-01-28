'''Programa que faça contagem regressiva para estouro de fogos de artifício
- de 10 a 0 com pausas de 1 segundo entre eles.'''
from time import sleep
from emoji import emojize
for contagem in range (10, -1, -1):
    print(contagem)
    sleep(1)
print(emojize('FELIZ ANO NOVO!!!:fireworks:'))