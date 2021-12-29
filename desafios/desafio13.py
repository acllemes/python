# faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Qual o valor do salário atual? '))
novo = salario + (salario * 15 / 100)
print('O seu salário era de R$ {:.2f} e com o aumento de 15% ficou R$ {:.2f}'.format(salario, novo))

