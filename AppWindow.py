# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setWindowIcon(QtGui.QIcon("homeIcon.jpg"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmButton.setGeometry(QtCore.QRect(61, 85, 181, 21))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 0, 91, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.redvalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.redvalue_input.setObjectName("redvalue_input")
        self.verticalLayout.addWidget(self.redvalue_input)
        self.greenvalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.greenvalue_input.setObjectName("greenvalue_input")
        self.verticalLayout.addWidget(self.greenvalue_input)
        self.bluevalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bluevalue_input.setObjectName("bluevalue_input")
        self.verticalLayout.addWidget(self.bluevalue_input)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 0, 100, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RedValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.RedValue.setObjectName("RedValue")
        self.verticalLayout_2.addWidget(self.RedValue)
        self.GreenValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.GreenValue.setObjectName("GreenValue")
        self.verticalLayout_2.addWidget(self.GreenValue)
        self.BlueValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.BlueValue.setObjectName("BlueValue")
        self.verticalLayout_2.addWidget(self.BlueValue)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 254, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Color App"))
        self.ConfirmButton.setText(_translate("MainWindow", "Get Color"))
        self.RedValue.setText(_translate("MainWindow", "Red Value"))
        self.GreenValue.setText(_translate("MainWindow", "Green Value"))
        self.BlueValue.setText(_translate("MainWindow", "Blue Value"))

def call_ui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

