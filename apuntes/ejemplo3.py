class Fecha: 
    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia
    
    def setDia(self, dia):
        if dia > 0 and dia < 32:
            self.__dia = dia
        else:
            print("Dia incorrecto")

def main():
    hoy = Fecha()

    print(hoy.getDia())
    hoy.setDia(5)
    print(hoy.getDia())
    hoy.setDia(50)
    print(hoy.getDia())

main()