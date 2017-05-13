'''
Created on 5 may. 2017

@author: MXCATEX
'''
import tkinter
from tkinter import *

def mcd():
    a=int(num1.get())
    b=int(num2.get())
    macd=0
    while b>0:
        macd=b
        b=a%b
        print(b)
        a=macd
        print("- ",a,"----",b)
    print("EL MCD ES ----->",a)       
    Label(ventana,text=str(a)).place(x=100,y=150)
    
ventana=Tk()
ventana.geometry("250x250")
num1=StringVar()
txtnum1=Entry(ventana,textvariable=num1)
txtnum1.place(x=100,y=10)
num2=StringVar()
lblnum1=Label(ventana,text="Numero 1").place(x=10,y=10)
lblnum2=Label(ventana,text="Numero 2").place(x=10,y=40)
txtnum2=Entry(ventana,textvariable=num2)
txtnum2.place(x=100,y=40)
imprime=Button(ventana,text="SACAR MCD ES :  ",command=mcd)
imprime.place(x=100,y=100)
ventana.mainloop()
