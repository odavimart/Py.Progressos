dias = int(input('Rodou quantos dias? '))
km = float(input('Rodou quantos km? '))
pago = (dias * 60) + (km * 0.15)
print('Total a pagar é de {:.2f}'.format(pago))