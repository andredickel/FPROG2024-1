#Solicita o valor da compra
valorcompra = float(input('Digite o valor de compra: R$'))

#Calcula o valor de desconto
desconto = valorcompra * 0.15

#Valor de compra com desconto
valordesconto = valorcompra - desconto

#Exibe o valor na tela
print('O valor da compra com desconto é: R$',valordesconto)