'''Escribir una función que le pasamos numero de filas y colunas
y devuelve una matriz bidimensional al azar con n filas y n 
columnas
Escribir una función que nos de la suma de las 
filas de la matriz'''
from random import randint

def matriz(filas, columnas):
    '''Se le pasan por parametro filas y columnas
    y devuelve una matriz bidireccional'''
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(randint(0, 9))
        matriz.append(fila)
    return matriz

def suma_filas(matriz):
    suma_fila = []
    for lista in matriz:
        suma_fila.append(sum(lista))
    return suma_fila

def suma_columnas(matriz, columnas):
    suma_columnas = []
    for i in range(columnas):
        suma = 0
        for lista in matriz:
            suma += lista[i]
        suma_columnas.append(suma)
    return suma_columnas

fila = int(input('Introduce las filas: '))
columna = int(input('Introduzca las columnas: '))
matriz = matriz(fila, columna)
print(matriz)
print(suma_filas(matriz))
print(suma_columnas(matriz, columna))