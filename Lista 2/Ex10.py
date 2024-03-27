#Informe o preço dos produtos
camiseta = 25.00
calças = 100.00
cintos = 40.00

#Informe o número de roupas compradas
num_camisetas = int(input('Informe a quantidade de camisetas compradas:'))
num_calças = int(input('Informe a quantidade de calças compradas:'))
num_cintos = int(input('Informe a quantidade de cintos comprados:'))

#Total compras
valorcompras = (num_camisetas * camiseta) + (num_calças * calças) + (num_cintos * cintos)

#Informe o valor com desconto
desconto = valorcompras * 0.10

#Valor total com desconto
valortotal = valorcompras - desconto

#Exiba na tela
print('Valor total do desconto:R$',desconto)
print('Valor total da compra com desconto:R$',valortotal)