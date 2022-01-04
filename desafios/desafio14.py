# escreva um programa que converta uma temperatura
# digitada em graus celsius e converta para graus fahrenheit

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = ((9 * celsius) / 5) + 32

# primeiro a multiplicação, divide por 5 e depois soma com 32, porém nesse programa não precisa usar os parenteses, ele calcula na sequencia da formula. Pq a ordem de precedencia é exatamente a ordem que os operadores aparecem.

print('A temperatura de {}°C corresponde a {}°F'.format(celsius, fahrenheit))

