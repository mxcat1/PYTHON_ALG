'''
Created on 8 may. 2017

@author: MAXCAT
'''
import tkinter
from tkinter import *
import TAREA_LUIGUI.combifuncion

def constructor():
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()

def combinatoria1():
    print(TAREA_LUIGUI.combifuncion.cobinatoria(num1.get(),num2.get()))
    Label(frmcombinatoria,text=TAREA_LUIGUI.combifuncion.cobinatoria(num1.get(),num2.get())).place(x=150,y=120)
    


frmcombinatoria=Tk()
constructor()
frmcombinatoria.geometry("250x150")
frmcombinatoria.title("Combinatoria de dos número")
lblnum1=Label(frmcombinatoria,text="NÚMERO1")
lblnum1.place(x=10,y=10)
txtnumero1=Entry(frmcombinatoria,textvariable=num1)
txtnumero1.place(x=100,y=10)
lblnum2=Label(frmcombinatoria,text="NUMERO2").place(x=10,y=40)
txtnumero2=Entry(frmcombinatoria,textvariable=num2).place(x=100,y=40)
btnmensaje=Button(frmcombinatoria,text="MENSAJE",command=combinatoria1)
btnmensaje.place(x=20,y=100)
lblrespuesta=Label(frmcombinatoria,text="LA COMBINATORIA ES : ").place(x=100,y=100)

frmcombinatoria.mainloop()
