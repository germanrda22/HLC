'''Cifrar un texto cambiando cada caracter por otro'''
clave = int(input('Introduzca el número para  modificar las letras: '))#Desplazamiento
texto = input('Introduzca un texto para cifrarlo: ')

def cifrado(texto, clave):
    texto_cifrado = ''

    for i in texto:
        num = ord(i)
        letra = chr(num + clave)
        texto_cifrado += letra
    return texto_cifrado

def cambia_letra(texto):
    texto_cambiado = ''

    caracter = texto[len(texto) - 1]
    texto_cambiado = caracter + texto.strip(caracter)
    return texto_cambiado

def invierte_cadena(texto):
    texto_invertido = ''
    for i in texto:
        texto_invertido = i + texto_invertido

    return texto_invertido

def invierte_cadena2(texto):
    return texto[::-1]

print(cifrado(texto, clave))
print(cambia_letra(texto))
print(invierte_cadena(texto))