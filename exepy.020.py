import math
co = float(input('Informe o número do Cateto Oposto: '))
ca = float(input('Informe o número do Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa é do valor de {:.2f}'.format(hi))