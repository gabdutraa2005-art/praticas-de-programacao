from  datetime import date
## alistamento
nascimento = int(input("Qual é o seu ano de nascimento?"))
idade =  date.today().year - nascimento 
falta =  18 - idade
prazo =  idade - 18
# se ele ainda vai se alisatar ao serviço militar, se tiver menos que 18 anos não passa
if idade <=17:
    print("Você foi não precisa se alistar, falta ainda {} anos".format(falta))
# se esta na hora do alismento, tiver 18 anos
elif idade ==18:
    print("Você precisa se alistar!")
# se já passou do tempo de se alistar
else:
    print('Você já passou do tempo! Tinha que se alistar a {} anos atrás.'.format(prazo))
# e o programa devera monstrar quando tempo falta ou passou do prazo do alistamento