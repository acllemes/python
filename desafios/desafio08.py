# escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimetros

medida = float(input('Uma distância em metros: '))
mm = medida * 1000 # milimetro
cm = medida * 100 # centimento
dm = medida * 10 # decimetro
dam = medida / 10 # decâmetro
hm = medida / 100 # hectômetro
km = medida / 1000 # quilometro
print('Você digitou {}, segue abaixo mais detalhes sobre a medida declarada'.format(medida))
print('Em milimetros é {}'.format(mm))
print('Em centimentos é {}'.format(cm))
print('Em decimetro é {}'.format(dm))
print('Em decâmetro é {}'.format(dam))
print('Em hectômetro é {}'.format(hm))
print('Em quilômetro é {}'.format(km))
