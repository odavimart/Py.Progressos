#Real para Dolar

real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 4.45
print('Com R${:.0f} você tem na carteira US{:.0f}'.format(real, dolar))
print('-'*16)

#Real para Euro

euro = real / 5.37
print('Com R${:.2f} você tem na carteira Eur{:.2f}'.format(real, euro))
print('-'*16)

#Real para Libra

libra = real / 6.27
print('Com R${:.2f} você tem na carteira GBT{:.2f}'.format(real, libra))
print('-'*16)

#Real para Ienes

iene = real / 0.033
print('Com R${:.2f} você tem na carteira JPY{:.2f}'.format(real, iene))
print('-'*16)

#Real para Yuan

yuan = real / 0.69
print('Com R${:.2f} você tem na carteira CNY{:.2f}'.format(real, yuan))
