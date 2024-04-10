import random

escolha = input('Escolha PAR ou IMPAR:').upper()

if escolha != 'PAR' and escolha != 'IMPAR':
    print('Escolha inválida, escolha entre PAR ou IMPAR')

else:
    numero = int(input('Escolha um número de 0 a 5:'))

    numero_aleatorio = random.randint(0, 5)

    soma = numero + numero_aleatorio

if soma % 2 == 0:
    resultado = 'PAR'

else:
    resultado = 'IMPAR'

if (escolha == 'PAR' and resultado == 'PAR') or (escolha == 'IMPAR' and resultado == 'IMPAR'):
    print('Você venceu! A soma é', resultado,'e o resultado da soma é',soma)

else:
    print('Você perdeu! A soma é',resultado,'e o resultado da soma é',soma)