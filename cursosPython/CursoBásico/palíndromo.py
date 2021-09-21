def palindromo(palabras):
    palabras = palabras.lower()
    palabras = palabras.replace('á','a')
    palabras = palabras.replace('é','e')
    palabras = palabras.replace('í','i')
    palabras = palabras.replace('ó','o')
    palabras = palabras.replace('ú','u')
    palabras = palabras.replace('-',' ')
    palabras = palabras.replace(' ','')
    return palabras == palabras[::-1]


def run():
    palabras = str(input('Escribre la/s palabra/s a evaluar: '))
    es_palindromo = palindromo(palabras=palabras)
    if es_palindromo:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()