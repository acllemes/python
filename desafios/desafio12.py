# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# 10*5/100 = 0.5
# 1500*10/100 = 150.0
# 875*15/100 = 131.25

preço = float(input('Qual é o valor do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R$ {:.2f}, com 5% de desconto fica R$ {:.2f}'.format(preço, novo))



