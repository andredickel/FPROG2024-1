import random

# Solicita ao usuário o número de faces do dado
num_faces = int(input("Quantas faces o dado deve ter (4, 6, 8, 10, 12 ou 16)? "))

# Verifica se o número de faces está entre as opções permitidas
if num_faces not in [4, 6, 8, 10, 12, 16]:
    print("Número de faces inválido. Por favor, escolha entre 4, 6, 8, 10, 12 ou 16.")
else:
    # Realiza o sorteio do dado
    resultado = random.randint(1, num_faces)
    print("O dado de", num_faces, "faces foi lançado e o resultado é:", resultado)