from time import sleep
velocidade = float(input('Que velocidade estava o carro? '))
print('PROCESSANDO...')
sleep(2)
if velocidade >80:
    print('MULTADO!')
    multa = (velocidade-80) * 7
    print('Você excedeu o limite de velocidade de 80km/h')
    print('Pagará um valor de R${:.2F}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
