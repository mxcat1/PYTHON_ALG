'''
Created on 12 may. 2017

@author: MAXCAT
'''
import tkinter
from tkinter import *

def fibonaci():
    num1=1
    num2=0
    posi=50
    while num1<=n.get() or num2<=n.get():
        Label(ventana,text=str(num2) + " - " + str(num1) + " - ").place(x=10,y=posi)
        num2=num2+num1
        num1=num2+num1
        posi=posi+30
    

ventana=Tk()
n=IntVar()
ventana.geometry("500x300")
ventana.title("SERIE FIBONACCI")
lblnum1=Label(ventana,text="INGRESE EL NUMERO PARA SABER HASTA DONDE SERA LA SERIE: ").place(x=10,y=10)
txtnum=Entry(ventana,textvariable=n).place(x=10,y=30)
btnfi=Button(ventana,text="CALCULAR",command=fibonaci).place(x=200,y=30)
ventana.mainloop()
