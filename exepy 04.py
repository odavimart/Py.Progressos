larg = float (input('Qual é a largura da parede: '))
alt =  float (input ('Qual é a altura da parede '))
area = larg * alt
print('A dimensão da parede é de {} x {} e a area de {}m²'.format(larg, alt, area))
tinta = area /2
print('Para pintar a parede será necessário {}L de tinta'.format(tinta))