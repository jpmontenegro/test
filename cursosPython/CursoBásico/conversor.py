def conversor(pesos, trm):
    pesos = input('驴C煤antos pesos ' + pesos + ' tienes: ')
    pesos = float(pesos)
    dolares = round(pesos/trm, 2)
    return dolares
    

menu = """
Bienvenido al converso de monedas 馃挼

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opci贸n: """

opcion = int(input(menu))

if opcion == 1:
    dolares = conversor(pesos = 'colombianos',trm = 4000)
    print('Tengo ' + str(dolares) + ' d贸lares')
elif opcion == 2:
    dolares = conversor(pesos = 'argentinos',trm = 65)
    print('Tengo ' + str(dolares) + ' d贸lares')
elif opcion == 3:
    dolares = conversor(pesos = 'mexicanos',trm = 20)
    print('Tengo ' + str(dolares) + ' d贸lares')
else: 
    print('Elige una opci贸n v谩lida, por favor')


