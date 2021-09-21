import random
import string

def generate_password(longitud):
    mayusculas = list(string.ascii_uppercase)
    minusculas = list(string.ascii_lowercase)
    simbolos = ['!','#','$','&','/','@']
    numeros = list('0')
    for i in range(1,10):
        numeros.append(str(i))
    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(longitud + 1):
        password.append(random.choice(caracteres))

    password = ''.join(password) #generan un string de todos los elementos de la lista password
    return password


def run():
    longitud = int(input('Ingresa la longitud deseada de tu nueva contraseña: '))
    password = generate_password(longitud = longitud)
    print('Tu nuerva contraseña es: ' + password)


if __name__ == '__main__':
    run()