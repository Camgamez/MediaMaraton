"""
Dentro del programa, este archivo es la parte del controlador que trae todas las ventanas y las ejecuta de manera
apropiada. A continuación se importan los archivos requeridos de PyQT y del View que se requieren para la interfaz de
usuario.
"""
from PyQt5 import QtWidgets
from View.mainwindow import Ui_MainWindow
from View.CarreraForm import Ui_CarreraForm
from View.ModuloAtleta import Ui_ModuloAtleta
from View.ResultadoCarrera import Ui_ResultadoCarrera
import sys


class MainWindow(QtWidgets.QMainWindow):
    """
    Este Main Window hace las veces de menú principal. Tiene Los botones necesarios para navegar por todas las
    funcionalidades y módulos del programa.
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goToModuloAtleta)
        self.ui.pushButton_2.clicked.connect(self.goToActualizarResultado)
        self.ui.pushButton_4.clicked.connect(self.goToClasificados)
        self.ui.pushButton_5.clicked.connect(self.goToResultadoCarrera)
        self.ui.pushButton_6.clicked.connect(self.goToCarreraForm)
        self.ui.closer.clicked.connect(self.closeAll)

    # Esta función permite cerrar el programa.
    def closeAll(self):
        stack.close()

    # Esta función lleva al módulo Crear Carrera
    def goToCarreraForm(self):
        stack.setCurrentIndex(stack.currentIndex() + 1)

    # Esta función lleva al módulo Atleta
    def goToModuloAtleta(self):
        stack.setCurrentIndex(stack.currentIndex() + 2)

    # Esta función lleva al módulo para crear resultado.
    def goToResultadoCarrera(self):
        stack.setCurrentIndex(stack.currentIndex() + 3)

    def goToActualizarResultado(self):
        stack.setCurrentIndex(stack.currentIndex() + 4)

    def goToClasificados(self):
        stack.setCurrentIndex(stack.currentIndex() + 5)


class CarreraForm(QtWidgets.QMainWindow):
    """
    Este es el  módulo de crear una nueva carrera. Solicita al usuario la información y la conecta con la base de datos.
    """
    def __init__(self):
        super(CarreraForm, self).__init__()
        self.ui = Ui_CarreraForm()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.goToMainWindow)

    def goToMainWindow(self):
        stack.setCurrentIndex(stack.currentIndex() - 1)


class ModuloAtleta(QtWidgets.QMainWindow):
    def __init__(self):
        super(ModuloAtleta, self).__init__()
        self.ui = Ui_ModuloAtleta()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.goToMainWindow)

    def goToMainWindow(self):
        stack.setCurrentIndex(stack.currentIndex() - 2)


class ResultadoCarrera(QtWidgets.QMainWindow):
    "Esta ventana permite crear un resultado"
    def __init__(self):
        super(ResultadoCarrera, self).__init__()
        self.ui = Ui_ResultadoCarrera()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.goToMainWindow)

    def goToMainWindow(self):
        stack.setCurrentIndex(stack.currentIndex() - 3)


class ActualizarResultado(QtWidgets.QMainWindow):
    """
    Esta ventana permite actualizar la información de un resultado ya generado.
    """
    def __init__(self):
        super(ActualizarResultado, self).__init__()
        self.ui = Ui_ResultadoCarrera()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.goToMainWindow)
        self.ui.label_3.setText("Actualizar Puesto")
        self.ui.label_4.setText("Actualizar Tiempo")
        self.ui.label_5.setText("Actualizar Clasificación")
        self.ui.label_6.setText("Actualizar Resultado:")

    def goToMainWindow(self):
        stack.setCurrentIndex(stack.currentIndex() - 4)


class Clasificados(QtWidgets.QMainWindow):
    """
    Esta ventana permite cambiar la clasificación de un atleta en un evento particular..
    """
    def __init__(self):
        super(Clasificados, self).__init__()
        self.ui = Ui_ResultadoCarrera()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.goToMainWindow)
        self.ui.label_3.hide()
        self.ui.lineEdit_3.hide()
        self.ui.label_4.hide()
        self.ui.lineEdit_4.hide()
        self.ui.label_6.hide()

    def goToMainWindow(self):
        stack.setCurrentIndex(stack.currentIndex() - 5)


app = QtWidgets.QApplication([])
stack = QtWidgets.QStackedWidget() # El stack contiene todas las ventanas
application = MainWindow()
carreraForm = CarreraForm()
moduloAtleta = ModuloAtleta()
resultadoCarrera = ResultadoCarrera()
actualizarResultado = ActualizarResultado()
clasificados = Clasificados()

stack.addWidget(application)
stack.addWidget(carreraForm)
stack.addWidget(moduloAtleta)
stack.addWidget(resultadoCarrera)
stack.addWidget(actualizarResultado)
stack.addWidget(clasificados)

stack.setFixedWidth(800)
stack.setFixedHeight(500)


stack.show()
sys.exit(app.exec())
