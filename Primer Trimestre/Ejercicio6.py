'''Función que le pasamos una cantidad y nos hace un desglose en monedas'''
cantidad = float(input('Introduzca una cantidad en euros'))

def desglosar_cantidad(cantidad):
    d = {}
    cantidades = [50000,20000,10000,5000,2000,1000,500,200,100, 50, 20, 10, 5, 2, 1]
    cantidad *= 100

    while cantidad != 0:
        for c in cantidades:
            d[c] = cantidad//c
            cantidad = cantidad % c
    return d
    
diccionario = desglosar_cantidad(cantidad)
for key in diccionario:
    print(key/100, diccionario[key])