# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showResultado.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowResultado(object):
    def setupUi(self, ShowResultado):
        ShowResultado.setObjectName("ShowResultado")
        ShowResultado.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(ShowResultado)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 1)
        self.popup_closer = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.popup_closer.setObjectName("popup_closer")
        self.gridLayout.addWidget(self.popup_closer, 3, 0, 1, 1)
        ShowResultado.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ShowResultado)
        self.statusbar.setObjectName("statusbar")
        ShowResultado.setStatusBar(self.statusbar)

        self.retranslateUi(ShowResultado)
        QtCore.QMetaObject.connectSlotsByName(ShowResultado)

    def retranslateUi(self, ShowResultado):
        _translate = QtCore.QCoreApplication.translate
        ShowResultado.setWindowTitle(_translate("ShowResultado", "Resultados Carrera"))
        self.pushButton_7.setText(_translate("ShowResultado", "Tiempo ASC"))
        self.pushButton_6.setText(_translate("ShowResultado", "Nombre ASC"))
        self.pushButton_5.setText(_translate("ShowResultado", "Apellido ASC"))
        self.pushButton_4.setText(_translate("ShowResultado", "Nacimiento ASC"))
        self.pushButton_3.setText(_translate("ShowResultado", "Pais ASC"))
        self.pushButton_2.setText(_translate("ShowResultado", "Ciudad ASC"))
        self.label.setText(_translate("ShowResultado", "Numero Evento:"))
        self.pushButton.setText(_translate("ShowResultado", "Consultar"))
        self.popup_closer.setText(_translate("ShowResultado", "Volver"))