# Jogo de encontrar o numero
# Objetivos:

# criar um algoritmo capaz de escolher um numero aleatório (OK)

# fazer com que esse algoritmo diga ao usuário uma estimativa de onde o numero se encontra (OK)

# fazer com que o usuário tente encontrar o numero até encontrar, e retornar para ele uma tela de vitória caso consiga(OK)

# Criar um interface gráfica para tudo isso ( )


import random

numero_aleatorio = random.randint(1, 1000)  # gera um numero aleatório

tentativas = 0

print('Bem vindo ao jogo de adivinhação')
print('Tente adivinhar o numero que estou pensando entre 1 e 1000')

while True:
    try:
        usuario_tentativas = int(input('Digite um numero: '))
    except ValueError:
        print('Digite apenas numeros')
        continue
    if usuario_tentativas == numero_aleatorio:
        print('Parabens voce acertou em ', tentativas, 'tentativas')
        break
    elif usuario_tentativas < numero_aleatorio:
        print('O numero que estou pensando e maior que', usuario_tentativas)
    else:
        print('O numero que estou pensando e menor que', usuario_tentativas)
    tentativas += 1
