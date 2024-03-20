#Valor smartphone
smartphone = 1000

#Valor tablet
tablet = 1500

quantidade = int(input('Digite a quantidade de smartphones vendidos:'))

quantidadetablet = int(input('Digite a quantidade de tablets vendidos:'))

valortotal = (quantidade * smartphone) + (quantidadetablet * tablet)

print('O valor total arrecadado é: R$',valortotal)