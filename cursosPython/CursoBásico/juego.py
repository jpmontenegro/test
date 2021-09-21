import random


def run():
    resultado = random.randint(1,100)
    numero = int(input('Elige un número entre 1 y 100: '))
    while resultado != numero:
        if resultado > numero:
            numero = int(input('Elige un número más grande: '))
        else:
            numero = int(input('Elige un número más pequeño: '))
    print('¡GANASTE!')


if __name__ == '__main__':
    run()