'''Crea una matriz bidimensional con f(fila) y c(columna),
escribe una función que tome como parámetro esa matriz y
devuelva las posiciones invertidas'''
from random import randint

def genera_matriz():
    '''Esta función genera una matriz de 3 * 4 '''
    lista = []
    for i in range(3):
        listaM = []
        for j in range(4):
            listaM.append(randint(1,10))
        lista.append(listaM)
    return lista

def lista_invertida(lista):
    lista_aux = lista.copy()
    lista_aux.reverse()
    return lista_aux

def invertir_matriz(matriz):
    matriz_aux = []
    n = len(matriz)
    for i in range(n):
        matriz_aux.append(lista_invertida(matriz[n - i - 1]))

    return matriz_aux

matriz = genera_matriz()
print(matriz)
print(invertir_matriz(matriz))