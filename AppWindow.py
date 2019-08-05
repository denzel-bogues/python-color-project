
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as p
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setWindowIcon(QtGui.QIcon("homeIcon.jpg"))


    def input_widgets(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 0, 91, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.redvalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.redvalue_input.setObjectName("redvalue_input")
        self.verticalLayout.addWidget(self.redvalue_input)
        red = self.redvalue_input.text()

        self.greenvalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.greenvalue_input.setObjectName("greenvalue_input")
        self.verticalLayout.addWidget(self.greenvalue_input)
        green = self.greenvalue_input.text()

        self.bluevalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bluevalue_input.setObjectName("bluevalue_input")
        self.verticalLayout.addWidget(self.bluevalue_input)
        blue = self.bluevalue_input.text()

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

        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmButton.setGeometry(QtCore.QRect(61, 85, 181, 21))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.clicked.connect(backend_stuff(red, green, blue))
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
    ui.input_widgets(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def backend_stuff(red, green, blue):
    data_read = p.read_csv("colors.csv", delimiter = ',', names=['Color names', 'Hex', 'R', 'G', 'B',])
# data_red = data_read[['R', 'G', 'B']]
    R = red
    G = green
    B = blue

    userdata = [R, G, B]
    user_df = p.DataFrame(userdata)
    in_read = p.DataFrame.transpose(p.DataFrame(user_df))
    in_read.columns = ['R', 'G', 'B']

    in_read['R'] = in_read['R'].astype(int)
    in_read['G'] = in_read['G'].astype(int)
    in_read['B'] = in_read['B'].astype(int)

def __main__():
    call_ui()
