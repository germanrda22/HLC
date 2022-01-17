'''Escribe una función a la que se le pasa una lista de números de tamaño n>1
Tenemos que buscar el punto de la lista en el que la sublista de la izquieda 
pesa lo mismo que la del lado derecho si no encuentra ningún punto balanceable 
devuelve none'''

def balanza(lista):
    if (len(lista) % 2 == 0 & len(lista) < 1):
        return None
    else:
        for mitad in range(1, len(lista)):
            if sum(lista[:mitad]) == sum(lista[mitad+1:]):
                return mitad
        return None

lista = [1, 2, 1, 5, 0, 4, 0]
print(balanza(lista))