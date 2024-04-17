valor_compra = float(input('Digite o valor da compra: R$'))

if valor_compra <= 20:
    lucro_percentual = 0.45
elif valor_compra <= 50:
    lucro_percentual = 0.35
else:
    lucro_percentual = 0.25

valor_venda = valor_compra * (1 + lucro_percentual)

print ('Valor aplicado com desconto: R$',valor_venda)