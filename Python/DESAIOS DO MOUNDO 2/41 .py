from  datetime import date
# verificar sobre idade do atleta de natação e de acordo com a idade dele monstrar categoria.
nascimento = int(input('Qual seu ano de nascimento?'))
idade = date.today().year - nascimento
if idade <=9:
    print('Sua categoria é a Mirim')
elif idade <=14:
    print('Sua categoria é Infantil')
elif idade <=19:
    print('Sua categoria é Junior')
elif idade == 20:
    print('Sua categoria é Senior')
else:
    print('Sua categoria é a master')