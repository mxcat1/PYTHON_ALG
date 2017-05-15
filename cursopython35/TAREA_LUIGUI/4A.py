'''
Created on 14 may. 2017

@author: MXCATEX
'''
import sys
import PyQt5
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


#Clase heredada de QmainWindow(Constructor de Ventanas)

class Ventana(QMainWindow):
    #Metodo Constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuracion del archivo uic
        uic.loadUi("MainWindows.ui",self)
        
#instancia para iniciar una aplicacion
app=QApplication(sys.argv)
#Creacion de un objeto de la clase
_ventana=Ventana()
#Mostrar Ventana
_ventana.show()
#ejecutar la aplicacion
app.exec_()
    

