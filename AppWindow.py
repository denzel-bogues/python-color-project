from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QFont
import pandas as p
import sys


class UiMainWindow(object):
    def __init__(self, MainWindow):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.verticalLayout_OutputWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)

        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)

        self.verticalLayout_Output = QtWidgets.QVBoxLayout(self.verticalLayout_OutputWidget)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.BlueValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.GreenValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.RedValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.bluevalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.greenvalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.redvalue_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 150)
        MainWindow.setMinimumSize(QtCore.QSize(400, 150))
        MainWindow.setMaximumSize(400, 200)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setWindowIcon(QtGui.QIcon("homeIcon.jpg"))
        self.__init__(MainWindow)

    def input_widgets(self, MainWindow):
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_OutputWidget.setGeometry(QtCore.QRect(250, 10, 100, 125))
        self.verticalLayout_OutputWidget.setObjectName("verticalLayout_OutputWidget")
        self.verticalLayout_Output.setContentsMargins(0, 0, 0, 00)
        self.verticalLayout_Output.setObjectName("verticalLayout_Output")

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 0, 91, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.redvalue_input.setObjectName("redvalue_input")
        self.verticalLayout.addWidget(self.redvalue_input)
        self.redvalue_input.setValidator(QIntValidator(0, 255))

        self.greenvalue_input.setObjectName("greenvalue_input")
        self.verticalLayout.addWidget(self.greenvalue_input)
        self.greenvalue_input.setValidator(QIntValidator(0, 255))

        self.bluevalue_input.setObjectName("bluevalue_input")
        self.verticalLayout.addWidget(self.bluevalue_input)
        self.bluevalue_input.setValidator(QIntValidator(0, 255))

        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 0, 100, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.RedValue.setObjectName("RedValue")
        self.verticalLayout_2.addWidget(self.RedValue)

        self.GreenValue.setObjectName("GreenValue")
        self.verticalLayout_2.addWidget(self.GreenValue)

        self.BlueValue.setObjectName("BlueValue")
        self.verticalLayout_2.addWidget(self.BlueValue)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 254, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.ConfirmButton.setGeometry(QtCore.QRect(61, 85, 181, 21))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.ConfirmButton.clicked.connect(lambda: self.backend_stuff())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Color App"))
        self.ConfirmButton.setText(_translate("MainWindow", "Get Color"))
        self.RedValue.setText(_translate("MainWindow", "Red Value"))
        self.GreenValue.setText(_translate("MainWindow", "Green Value"))
        self.BlueValue.setText(_translate("MainWindow", "Blue Value"))

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())
        else:
            pass

    def add_label(self, text):
        color_text = QtWidgets.QLabel()
        color_text.setText(text)
        color_text.setFont(QFont('Arial', 8))
        color_text.setWordWrap(True)
        self.clearLayout(self.verticalLayout_Output)
        self.verticalLayout_Output.addWidget(color_text)

    def backend_stuff(self):
        data_read = p.read_csv("colors.csv", delimiter=',', names=['Color names', 'Hex', 'R', 'G', 'B'])

        if self.redvalue_input.text() != "":
            R = int(self.redvalue_input.text())
        else:
            R = -1

        if self.greenvalue_input.text() != "":
            G = int(self.greenvalue_input.text())
        else:
            G = -1

        if self.bluevalue_input.text() != "":
            B = int(self.bluevalue_input.text())
        else:
            B = -1

        if R >= 0 and G >= 0 and B >= 0:
            userdata = [R, G, B]

            user_df = p.DataFrame(userdata)

            in_read = p.DataFrame.transpose(p.DataFrame(user_df))
            in_read.columns = ['R', 'G', 'B']
        
            desired_df = p.merge(data_read, in_read, on=['R', 'G', 'B'], how='inner')
            if not desired_df.empty:
                color_string = p.Series.to_string(desired_df['Color names'])

                self.add_label(color_string)
            else:
                err_text = "No Color\n Found,\n Try Again"
                self.add_label(err_text)
        else:
            err_text = "please insert RGB values\n to get Color"
            self.add_label(err_text)


def call_ui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow(MainWindow)
    ui.setupUi(MainWindow)
    ui.input_widgets(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

call_ui()
