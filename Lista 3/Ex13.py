# Solicita as notas dos graus A e B
nota_a = float(input("Digite a nota do Grau A: "))
nota_b = float(input("Digite a nota do Grau B: "))

# Calcula a média inicial
media_inicial = (nota_a + nota_b) / 2

# Verifica se o aluno passou por média ou ficou em recuperação
if media_inicial >= 6.0:
    print("Média final:", media_inicial)
    print("Aluno aprovado!")
else:
    print("Média final:", media_inicial)
    substituir = input("O aluno ficou em recuperação. Deseja substituir o Grau A ou o Grau B? (Digite 'a' ou 'b'): ")
    if substituir == 'a':
        nota_a = float(input("Digite a nota do Grau C: "))
    elif substituir == 'b':
        nota_b = float(input("Digite a nota do Grau C: "))
    else:
        print("Opção inválida. Encerrando o programa.")
        exit()