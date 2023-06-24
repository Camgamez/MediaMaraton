'''
Programación orientada a objetos. Creación de clases.
'''

class atleta: 
    def __init__(self, nombre, edad): 
         self.nombre = nombre
         self.edad = edad


# def main():
    ejemplo = atleta("pepe pegoreto", 25)
    print(id(ejemplo))
    print(ejemplo.nombre)
    print(ejemplo.edad)

    ejemplo2 = atleta("Pepito", 5)
    print(id(ejemplo2))
    print(ejemplo2.nombre)
    print(ejemplo2.edad)

    ejemplo2 = ejemplo
    ejemplo2.nombre = "Pepi"
    print(id(ejemplo2))
    print(ejemplo2.nombre)
    print(ejemplo2.edad)

