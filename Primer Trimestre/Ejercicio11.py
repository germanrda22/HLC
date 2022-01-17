'''String de 4 posiciones numericas aleatorio y que no se repita el numero.
    será oculto. intentamos adivinarlo. Mostrará aciertos y coincidencias.
    La coincidencia es que haya numeros iguales que el oculto
'''
from random import randint
def crearNumero():
    '''Esta funcion crea un numero aleatorio
    de 4 digitos y que no repite numeros'''
    objetivo = ''
    while len(objetivo) != 4:
        numero = randint(0,9)
        if(str(numero) not in objetivo):
            objetivo += str(numero)
    return objetivo

def analiza(entrada, objetivo):
    aciertos = 0
    coincidencias = 0
    for i in range(4):
        n_entrada = entrada[i]
        n_objetivo = objetivo[i]

        if n_entrada == n_objetivo:
            aciertos += 1
        
        if n_entrada in objetivo:
            coincidencias += 1
    return (aciertos, coincidencias)

def jugar():
    objetivo = crearNumero()
    entrada = input('Introduzca un numero de 4 digitos')    