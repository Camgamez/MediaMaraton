# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarreraForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CarreraForm(object):
    def setupUi(self, CarreraForm):
        CarreraForm.setObjectName("CarreraForm")
        CarreraForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CarreraForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 90, 631, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 10, 2, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout.addWidget(self.textEdit_4, 6, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 2, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 7, 1, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout.addWidget(self.textEdit_5, 8, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout.addWidget(self.textEdit_3, 4, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 11, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 50, 441, 22))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 430, 107, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        CarreraForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarreraForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        CarreraForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CarreraForm)
        self.statusbar.setObjectName("statusbar")
        CarreraForm.setStatusBar(self.statusbar)

        self.retranslateUi(CarreraForm)
        QtCore.QMetaObject.connectSlotsByName(CarreraForm)

    def retranslateUi(self, CarreraForm):
        _translate = QtCore.QCoreApplication.translate
        CarreraForm.setWindowTitle(_translate("CarreraForm", "MainWindow"))
        self.label_4.setText(_translate("CarreraForm", "¿Cuál es el valor del segundo premio?"))
        self.label_3.setText(_translate("CarreraForm", "¿Cuál es el valor del primer premio?"))
        self.pushButton.setText(_translate("CarreraForm", "Guardar"))
        self.label_2.setText(_translate("CarreraForm", "¿Cuál es el año del evento?"))
        self.label_5.setText(_translate("CarreraForm", "¿Cuál es el valor del tercer premio?"))
        self.label.setText(_translate("CarreraForm", "¿Cuál es en número del evento?"))
        self.label_6.setText(_translate("CarreraForm", "Habilitar Nueva Carrera"))
        self.pushButton_2.setText(_translate("CarreraForm", "Volver"))
