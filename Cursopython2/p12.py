'''
Created on 24 de jun. de 2016

@author: Mxcatv
'''
import os
import Tkinter
from Tkinter import *
import tkFileDialog

def seleco():
    global c
    c=tkFileDialog.askdirectory(title="Selecione una carpeta")
    global p
    p = r"%s"%(c)
    global la
    la= []
    global ld
    ld = os.walk(p)

def nomb():
    nnmb=nmu.get()
    i = 1
    nb = []

    for root, dirs, files in ld:
        for fh in files:
            (nomFichero,extension) = os.path.splitext(fh)
            la.append(nomFichero+extension)
            nvm = "%s 00%d%s"%(nnmb,i,extension)
            i = i+1
            nb.append(nvm)

    print(nb)
    print(la)
    contador = len(la)
    for x in range(contador):
        os.rename(os.path.join(p, la[x]),os.path.join(p,nb[x]))
    
v=Tk()
v.title("Modificador Archivos")
v.geometry("500x300")
v.configure(background="#00FFFF")

l1=Label(v,text="Haga click en el boton para Selecionar una carpeta",font=("Algerian",12))
l1.place(x=25,y=80)

b=Button(v,text="Selecione su carpeta",command=seleco)

b.place(x=180,y=120)

b2=Button(v,text="Cambiar",command=nomb)
b2.place(x=220,y=250)
nmu=StringVar()
nnmb=nmu.get()
l2=Label(v,text="Indique el nuevo nombre para tus archivos",font=("Algerian",12))
l2.place(x=65,y=170)
Entry(v,textvariable=nmu,width=50).place(x=100,y=220)

v.mainloop()
