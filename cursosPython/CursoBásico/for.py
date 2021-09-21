# contador = 1
# print(contador)
# while contador < 10:
#     contador += 1
#     print(contador)


# range por default parte del 0
# for contador in range(1,11):
#     print(contador)
# for contador in list(range(1,11)):
#     print(contador)

# for letra in str('hola perra'):
#     print(letra)


def run():
    frase = input('Escribe una frase: ')
    for letra in frase:
        print(letra.upper())


if __name__ == '__main__':
    run()