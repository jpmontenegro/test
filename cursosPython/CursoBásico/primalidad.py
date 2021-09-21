def factorial(numero):
    respuesta = 1
    while numero > 1:
        respuesta *= numero
        numero -= 1
    return respuesta


def num_primo(numero):
    # contador = 0
    # for i in range(1, numero + 1):
    #     if i == 1 or i == numero:
    #         continue
    #     if numero % i == 0:
    #         contador +=1
    # return contador == 0

    # Teorema de John Wilson
    if(numero == 1):
        return True
    else:
        return (factorial(numero -1) + 1) % numero == 0


def run():
    numero = int(input('Escribe un número: '))
    if num_primo(numero=numero):
        print('Es un número primo')
    else: 
        print('No es un número primo') 


if __name__ == '__main__':
    run()