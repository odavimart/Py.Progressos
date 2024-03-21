from random import randint
from time import sleep
computador = randint(0,20)
jogador = int(input('Qual número você escolheu? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! VCOÊ ACERTOU!')
else:
    print('VOCÊ ERROU! HAHAHA ><')
    print('O número que escolhi foi {} e você {}.'.format(computador, jogador))
    print('TENTE NOVAMENTE!')