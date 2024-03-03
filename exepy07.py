salário =float(input('Qual é o seu salário? R$'))
dinheiro = salário + (salário * 15 / 100)
print('Com o reajuste salarial, com aumento de 15%, o seu salário de {:.2f}, passará a ser {:.2f}'.format(salário, dinheiro))