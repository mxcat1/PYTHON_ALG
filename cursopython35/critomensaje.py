'''
Created on 22 de jun. de 2016

@author: Mxcatv
'''
from tkinter import *
clbg = "#B9AAFF"
v = Tk()
v.title("Encrptacion de Mensajes")
v.geometry("400x300")
v.iconbitmap(r"pro.ico")
v.configure(background="red")
def descrip():
    w = n.get()
    w=w.upper()
    k = int(llave.get())
    l = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    r1 = ""
    for s in w:
        if s in l:
            num = l.find(s)
            num = num - k
            if num >=len(l):
                num = num - len(l)
            elif num < 0:
                num = num + len(l)

            r1 = r1 + l[num]
        else:
            r1 = r1 + s
    Label(v,text=r1,bg="white",font=("Impact Normal",13)).place(x=30,y=240)
    print(r1)
def encriptar():
    w = n.get()
    w=w.upper()
    k = int(llave.get())
    l = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    r = ""
    for s in w:
        if s in l:
            num = l.find(s)
            num = num + k
            if num >=len(l):
                num = num - len(l)
            elif num < 0:
                num = num + len(l)
            r = r+l[num]
        else:
            r = r + s
    
    Label(v,text=r,bg="white",font=("Impact Normal",13)).place(x=30,y=160)
    print(r)

n = StringVar()

llave=StringVar()

Label(v,text="Escriba un mensaje a encriptar o Desencriptar",bg="red",fg="#FFFFFF",font=("Impact Normal",13)).place(x=10,y=10)
Label(v,text="Indique la llave",bg="red",fg="#FFFFFF",font=("Impact Normal",13)).place(x=10,y=90)
Label(v,text="Mensaje Encriptado",bg="red",fg="#FFFFFF",font=("Impact Normal",10)).place(x=130,y=120)
Label(v,text="Mensaje",bg="red",fg="#FFFFFF",font=("Impact Normal",13)).place(x=10,y=50)
Label(v,text="Mensaje Desencriptado",bg="red",fg="#FFFFFF",font=("Impact Normal",10)).place(x=130,y=200)
b = Button(v,text="ENCRIPTAR",command=encriptar)
b1 = Button(v,text="DENCRIPTAR",command=descrip)
b1.place(x=30,y=200)
b.place(x=30,y=120)
Entry(v,textvariable=n,width=40).place(x=130,y=50)
Entry(v,textvariable=llave,width=5).place(x=130,y=90)
v.mainloop()
