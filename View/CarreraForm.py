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
        CarreraForm.resize(889, 741)
        self.centralwidget = QtWidgets.QWidget(CarreraForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 90, 631, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 2, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 50, 441, 22))
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        CarreraForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarreraForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 32))
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
        self.label_3.setText(_translate("CarreraForm", "¿Cuál es el valor del primer premio?"))
        self.label_5.setText(_translate("CarreraForm", "¿Cuál es el valor del tercer premio?"))
        self.pushButton.setText(_translate("CarreraForm", "Guardar"))
        self.label_2.setText(_translate("CarreraForm", "¿Cuál es el año del evento?"))
        self.label.setText(_translate("CarreraForm", "¿Cuál es en número del evento?"))
        self.label_4.setText(_translate("CarreraForm", "¿Cuál es el valor del segundo premio?"))
        self.pushButton_2.setText(_translate("CarreraForm", "Volver"))
        self.label_6.setText(_translate("CarreraForm", "Habilitar Nueva Carrera"))
