from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from ui_Regstarion_Form import Ui_MainWindow
import sys


class myApp(QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        #self.setupUi(self)
        uic.loadUi("E:/Gradution Project/New folder/Python_Files/Regstarion_Form.ui",self)
        self.show()


#if __name__ == "__main__":


app= QApplication(sys.argv)
RegForm=myApp()

#ui=Ui_MainWindow()
#ui.setupUi(Form)
RegForm.show()
app.exec_()
