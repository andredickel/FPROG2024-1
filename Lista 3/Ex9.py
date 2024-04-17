cotacao_real_para_euro = float(input("Digite a cotação do Euro em relação ao Real: "))
cotacao_real_para_dolar = float(input("Digite a cotação do Dólar em relação ao Real: "))

# Apresenta o menu de opções
print("\nMenu:")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

# Solicita a escolha do usuário
opcao = int(input("Escolha uma opção: "))

# Realiza a conversão de acordo com a opção escolhida
if opcao == 1:
    valor_real = float(input("Digite o valor em Reais: "))
    valor_convertido = valor_real / cotacao_real_para_euro
    print("Valor em Euros:", valor_convertido)
elif opcao == 2:
    valor_real = float(input("Digite o valor em Reais: "))
    valor_convertido = valor_real / cotacao_real_para_dolar
    print("Valor em Dólares:", valor_convertido)
elif opcao == 3:
    valor_euro = float(input("Digite o valor em Euros: "))
    valor_convertido = valor_euro * cotacao_real_para_dolar
    print("Valor em Dólares:", valor_convertido)
elif opcao == 4:
    valor_euro = float(input("Digite o valor em Euros: "))
    valor_convertido = valor_euro * cotacao_real_para_euro
    print("Valor em Reais:", valor_convertido)
elif opcao == 5:
    valor_dolar = float(input("Digite o valor em Dólares: "))
    valor_convertido = valor_dolar * (1 / cotacao_real_para_dolar)
    print("Valor em Euros:", valor_convertido)
elif opcao == 6:
    valor_dolar = float(input("Digite o valor em Dólares: "))
    valor_convertido = valor_dolar * (1 / cotacao_real_para_dolar)
    print("Valor em Reais:", valor_convertido)
else:
    print("Opção inválida")