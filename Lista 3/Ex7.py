salario = float(input('Digite o salário do funcionário: R$'))

desconto_maximo = 318.20
desconto_proporcional = salario * 0.11

if desconto_proporcional > desconto_maximo:
    desconto = desconto_maximo

else:
    desconto = desconto_proporcional

print('O desconto providenciário é: R$',desconto)