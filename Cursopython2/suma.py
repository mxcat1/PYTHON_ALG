'''
Created on 24 jun. 2016

@author: Mxcatv
Programa que suma dos valores o numero enteros
'''
import Tkinter
import tkMessageBox as tms
from Tkinter import *

def suma():
    sum=float(n1.get())+float(n2.get())
    #sum=int(n1.get())+int(n2.get())
    lblrpt=Label(vent,text=str(sum)).place(x=80,y=150)
    tms.showinfo("Respuesta", sum)

vent=Tk()
vent.geometry("200x200")
vent.configure(background="red")
btnsuma=Button(vent,text="Sumar",command=suma)
btnsuma.place(x=80,y=80)
n1=StringVar()
n2=StringVar()
txtnum1=Entry(vent,textvariable=n1,width=10).place(x=25,y=40)
txtnum2=Entry(vent,textvariable=n2,width=10).place(x=110,y=40)
Label(vent,text="La Respuesta es").place(x=60,y=120)
lblrpt=Label(vent,text=" ").place(x=80,y=150)
vent.mainloop()