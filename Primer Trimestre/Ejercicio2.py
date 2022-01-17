import math

def aplica_in_place(funcion, datos):
    '''Aplica una función a una lista de datos'''
    for i in range(len(datos)):
        datos[i] = funcion(datos[i])

def procesa_in_place(acciones, datos):
    '''Aplica una lista de acciones a una lista de datos'''
    for funcion in acciones:
        aplica_in_place(funcion, datos)

def aplica(funcion, datos):
    '''Devuelve una lista tras aplicar una función a una lista de datos'''
    return [funcion(dato) for dato in datos]

def procesa(acciones, datos):
    '''Devuelve una lista tras aplicar una lista de funciones a una
    lista de datos'''
    datos_aux = datos.copy()

    for i in range(len(datos_aux)):
        for funcion in acciones:
            datos_aux[i] = funcion(datos_aux[i])

    return datos_aux

datos = [-9, -4, 8, 13.5, 78, 1, 0]
acciones = [abs, math.sqrt]
lista = procesa([abs, math.sqrt], [-9, -4])
aplica_in_place(abs, datos)