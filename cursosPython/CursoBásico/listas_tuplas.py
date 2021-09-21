# Listas
numeros = [1,3,4,5]
objetos = ['hola',3,4.5,True]
objetos[0:3:2]
objetos[::-1]
objetos.append(False) # métodos de las listas
objetos.pop(len(objetos)+1) #se elimina el objeto del índice 4 (posición 5)

for elementos in objetos:
    print(elementos)

numeros2 = [5,3,5,6]

lista_final = numeros + numeros2
numeros*5

# Tuplas (objetos inmutables)
tupla = (1,2,3,4)
tupla2 = ('hola',3,4)
# no funcionan las funciones .append y .pop
# los loops son más rapidos con tuplas
for numero in tupla:
    print(numero)
