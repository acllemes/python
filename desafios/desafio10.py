# conversor de moedas criar um programa que leia quanto dinheiro a pessoa
# tem na carteira e quanto dolares ela pode comprar

# 5,64

real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.64
print('Com R$ {:.2f} reais você pode comprar U$ {:.2f} dolares.'.format(real, dolar))



