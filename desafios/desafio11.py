#faça um programa que leia a largura e a algura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessaria para pinta-lá.
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} de largura x {} altura e sua área é de {} m2'.format(largura, altura, area))
print('Você vai precisar de {} litros de tinta para pintar a parede.'.format(tinta))
