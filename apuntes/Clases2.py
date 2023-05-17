
class Instrumento: 
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print("Estamos tocando musica")

    def romper(self):
        print('El instrumento esta roto \n'
              'Se debe pagar $' + str(self.precio) + ' para repararlo.')
        
class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    def __init__(self, precio, prec_cuerda):
        super().__init__(precio)
        self.prec_cuerda = prec_cuerda
        
class Terrestre():
    def desplazarse(self):
        print("El animal anda...")

class Acuatic():
    def desplazarse(self):
        print("El animal nada...")

class Cocodrilo(Acuatic, Terrestre):
    pass

class Ejemplo: 
    def publico(self): 
        print("Publico")
    def __privado(self): 
        print("Privado")
    def _privado(self): 
        print("Privado mangled")


def main():

    """
    guitarra = Guitarra(1000, 42)
    guitarra.tocar()
    guitarra.romper()
    print("El Instrumento es una: ", type(guitarra).__name__, " y las cuerdas cuestan: ", guitarra.prec_cuerda)

    bateria = Bateria(5000)
    bateria.tocar()
    bateria.romper()
    
    totodile = Cocodrilo()
    totodile.desplazarse()
    """
    ejemplo = Ejemplo()
    ejemplo.publico()
    ejemplo._privado()
main()