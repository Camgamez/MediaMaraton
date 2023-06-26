"""
Dentro del programa, este archivo es la parte del controlador que trae todas las ventanas y las ejecuta de manera
apropiada. A continuación se importan los archivos requeridos de PyQT y del View que se requieren para la interfaz de
usuario.
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QModelIndex, Qt
from View.mainwindow import Ui_MainWindow
from View.CarreraForm import Ui_CarreraForm
from View.ModuloAtleta import Ui_ModuloAtleta
from View.ResultadoCarrera import Ui_ResultadoCarrera
from View.ShowResultado import Ui_ShowResultado
from model import main
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
        self.ui.pushButton_3.clicked.connect(self.goToCheckResult)
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

    # Esta funcion nos lleva a consultar resultado
    def goToCheckResult(self):
        stack.setCurrentIndex(stack.currentIndex() + 6)


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

# This function defines the showResultado window
class ShowResultado(QtWidgets.QMainWindow):
    def __init__(self):
        super(ShowResultado, self).__init__()
        self.ui = Ui_ShowResultado()
        self.ui.setupUi(self)
        # Call object from Clasificacion in main and the sql conection 
        self.clasificacionObj = main.Clasificacion()
        self.conSQL = main.conexion_sql()

        # Button that stores the num_event to search
        self.ui.pushButton.clicked.connect(self.returnLineEdit)

        # Connection between orderbuttons and order of the search
        self.ui.pushButton_7.clicked.connect(self.showTiempoC)
        self.ui.pushButton_6.clicked.connect(self.showNombre)
        self.ui.pushButton_5.clicked.connect(self.showApellido)
        self.ui.pushButton_4.clicked.connect(self.showNacimiento)
        self.ui.pushButton_3.clicked.connect(self.showPais)
        self.ui.pushButton_2.clicked.connect(self.showCiudad)

        # The previous menu button
        self.ui.popup_closer.clicked.connect(self.goToMainWindow)
    
    def goToMainWindow(self):
        stack.setCurrentIndex(stack.currentIndex() - 6)
    
    # Function to store the lineEdit input to a value on clasificacionObj
    def returnLineEdit(self):
        self.clasificacionObj.set_evento(self.ui.lineEdit.text())

    # Each of this functions is a order in the search 
    def showTiempoC(self):
        self.clasificacionObj.set_option(1)
        self.clasificacionObj.consultar_clasificacion(self.conSQL)
        self.data = self.clasificacionObj.get_tabla()
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)
    
    def showNombre(self):
        self.clasificacionObj.set_option(2)
        self.clasificacionObj.consultar_clasificacion(self.conSQL)
        self.data = self.clasificacionObj.get_tabla()
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)

    def showApellido(self):
        self.clasificacionObj.set_option(3)
        self.clasificacionObj.consultar_clasificacion(self.conSQL)
        self.data = self.clasificacionObj.get_tabla()
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)

    def showNacimiento(self):
        self.clasificacionObj.set_option(4)
        self.clasificacionObj.consultar_clasificacion(self.conSQL)
        self.data = self.clasificacionObj.get_tabla()
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)

    def showPais(self):
        self.clasificacionObj.set_option(5)
        self.clasificacionObj.consultar_clasificacion(self.conSQL)
        self.data = self.clasificacionObj.get_tabla()
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)

    def showCiudad(self):
        self.clasificacionObj.set_option(6)
        self.clasificacionObj.consultar_clasificacion(self.conSQL)
        self.data = self.clasificacionObj.get_tabla()
        self.model = TableModel(self.data)
        self.ui.tableView.setModel(self.model)

# This class stablish how will the table create from data of a list of lists
class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        # Number of columns
        return len(self._data[0])

app = QtWidgets.QApplication([])
"""
El stack es una lista de objetos. 
Cada objeto es una instanciación de una ventana diferente.   
"""
stack = QtWidgets.QStackedWidget()

# A continuación están las ventanas instanciadas.
application = MainWindow()
carreraForm = CarreraForm()
moduloAtleta = ModuloAtleta()
resultadoCarrera = ResultadoCarrera()
actualizarResultado = ActualizarResultado()
clasificados = Clasificados()

showResultadoObj = ShowResultado()

# Aquí se agregan las ventanas en el stack
stack.addWidget(application)
stack.addWidget(carreraForm)
stack.addWidget(moduloAtleta)
stack.addWidget(resultadoCarrera)
stack.addWidget(actualizarResultado)
stack.addWidget(clasificados)
stack.addWidget(showResultadoObj)

stack.setFixedWidth(1000)
stack.setFixedHeight(1000)

# Main model
con = main.conexion_sql()
main.crearSQLTables(con)


stack.show()
sys.exit(app.exec())
