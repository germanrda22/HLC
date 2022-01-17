'''Haz una función que admite un número entero como  
parámetro y devuelve ese número en binario'''

def binario(num):
    binario = ''
    while num  // 2 != 0:
        resto = num % 2 
        binario = str(resto) + binario
        num //= 2
        if num == 0:
            opcion = False
    return str(num) + binario

def octal(num):
    pass

def hexadecimal(num):
    pass

num = int(input('Introduzca un número'))
print(binario(num))