# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moduloAtleta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModuloAtleta(object):
    def setupUi(self, ModuloAtleta):
        ModuloAtleta.setObjectName("ModuloAtleta")
        ModuloAtleta.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ModuloAtleta)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 60, 511, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 2)
        ModuloAtleta.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModuloAtleta)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 32))
        self.menubar.setObjectName("menubar")
        ModuloAtleta.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModuloAtleta)
        self.statusbar.setObjectName("statusbar")
        ModuloAtleta.setStatusBar(self.statusbar)

        self.retranslateUi(ModuloAtleta)
        QtCore.QMetaObject.connectSlotsByName(ModuloAtleta)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Volver"))
        self.pushButton_2.setText(_translate("MainWindow", "Modificar atleta"))
        self.pushButton.setText(_translate("MainWindow", "Registrar un nuevo atleta"))
        self.pushButton_3.setText(_translate("MainWindow", "Consultar atleta"))