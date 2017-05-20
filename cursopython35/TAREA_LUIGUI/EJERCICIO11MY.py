'''
Created on 19 may. 2017

@author: MAXCAT
'''
#!/urs/bin/env python
# -*- coding: utf-8-*-
import tkinter
import sqlite3
from tkinter import *
from TAREA_LUIGUI.persona import persona
from sqlite3 import *

persona1=persona()

def ingresar():
    cone=sqlite3.connect("contacto.db3")
    cmd=cone.cursor()
    persona1.ingreso("Pedro", "Vilca", "CALLE 1", "15-03-17")
    reg=(3,persona1.nombre,persona1.apellido,persona1.fecha)
    cmd.execute("INSERT INTO contacto VALUES(?,?,?,?)",reg)
    cone.commit()

#ingresar()
    
'''cone=sqlite3.connect('contacto.db3')
cmd=cone.cursor()
print("SE ABRIO CORRECTAMENTE")

cmd.execute("select * from contacto")

for registro in cmd:
    print(registro[0])
    print(registro[1])
    print(registro[2])
    print(registro[3])
'''

ventana=Tk()
ventana.title("AGENDA")
ventana.geometry("400x300")
lblnombre=Label(ventana,text="NOMBRE").place(x=10,y=10)
ventana.mainloop()