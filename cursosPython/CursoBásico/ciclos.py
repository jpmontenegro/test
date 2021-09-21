def run():
    ejemplo = input(str("""
    Ejemplos de ciclos:
    
    1 - Continue
    2 - Break en números
    3 - Break en texto
    4 - Juego

    Selecciona el ejemplo a probar: """))
    if ejemplo == str(1):
        for contador in range(100):
            if contador % 2 != 0:
                continue
            print(contador)

    elif ejemplo == str(2):
        for i in range(100):
            print(i)
            if i == 50:
                break

    elif ejemplo == str(3):
        texto = input('Escribe un texto: ')
        texto = texto.lower()
        for letra in texto:
            if letra == 'o':
                break
            print(letra)

    else:
        numero = int(input(str("""
        Vamo' a juga:

        Elige un número entre el 1 y el 100 y te mostraré toda la secuencia 
        de número que son multiplos del número que elegiste: """)))
        contador = 1
        while contador <= 100:
            contador += 1
            if (contador-1)  % numero != 0:
                continue
            print(contador-1)
                

if __name__ == '__main__':
    run()