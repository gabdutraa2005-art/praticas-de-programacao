l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))