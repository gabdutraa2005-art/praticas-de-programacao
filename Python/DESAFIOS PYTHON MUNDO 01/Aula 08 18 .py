from maht import radians, sin, cos, tan
a = float(input('Digite um ângulo: '))
print('Digitando o ângulo {} temos:'.format(a))
print('O seno é: {:.2f}'.format(sin(radians(a))))
print('O cosseno é: {:.2f}'.format(cos(radians(a))))
print('A tangente é: {:.2f}'.format(tan(radians(a))))