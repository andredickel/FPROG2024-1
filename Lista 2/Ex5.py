#Informe o preço do litro da gasolina
gasolina = 5.35

#Informe o valor disponivel para abastecer
valor = float(input('Digite o valor disponivel para abastecer:R$'))

litro = valor / gasolina

#Informe o quantos litros será possivel abastecer
print('Com R$',valor, 'será possivel abastecer',litro,'litros')