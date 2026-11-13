# preciso fazer uma programa aonde a pessoa digita o sexo so que somente com M ou F.
sexo = 'Ff' or 'Mm'
while sexo:
    sexo = str(input('Digite o seu sexo [M/F]: '))
    if sexo in 'FfMm':
        print('Tudo certo!')
else:
    print('Tente novamente')