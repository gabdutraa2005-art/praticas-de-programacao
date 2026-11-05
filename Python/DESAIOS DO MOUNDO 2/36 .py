casa = float(input("Qual é o valor que você precisa?"))
salario = float(input("Qual o seu salario?"))
anos = float(input("Em quantos anos você pretende pagar a sua casa?"))
limite = salario * 0.30
# Aqui fiz com que eu descobrisse quantos por mẽs ele iria precisar pagar
juros = anos * 12
juros2= casa / juros
# indicador: se a parcela for menor que 30% do salario, vai dar o output
if juros2 < limite:
    print("É com grande prazar que anuncios que você foi aprovado!")
    print("Sua parcela ficara {:.2f} e você vai pagar em {:.1f} meses".format(juros2,juros))
# indicado:  se a parcela for maior que o 30% do salario, vai dar o output
else:
    print("Reprovado")