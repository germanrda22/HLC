'''
Definir la clase cola 
Cola: contenido(list), guardar(elemento), saca(), vacia()bool
Definir la clase pila
Pila: contenido(list), guardar(algo), saca(), vacia()bool, cima()
'''
class Cola:
    def __init__(self):
        self.cola = []
        self.vacia = True

    def guardar(self, elemento):
        self.cola.append(elemento)

    def saca(self):
        self.cola.pop()

    def vacia(self):
        if (len(self.cola) >= 1):
            self.vacia = False

class Pila:
    def __init__(self):
        pass

    def guardar():
        pass

    def sacar():
        pass

    def vacia():
        pass

    def cima():
        pass