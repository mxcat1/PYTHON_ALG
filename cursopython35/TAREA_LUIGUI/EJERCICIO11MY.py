'''
Created on 19 may. 2017

@author: MAXCAT
'''
#!/urs/bin/env python
# -*- coding: utf-8-*-
import tkinter
import sqlite3
from tkinter import *
from persona import persona
from sqlite3 import *

persona1=persona()

def ingresar():
    try:
        cone=sqlite3.connect("contacto.db3")
        cmd=cone.cursor()
        #cmd1=cone.cursor()
        persona1.ingreso(nombre.get(), apellido.get(), direccion.get(), fecha.get())
        '''cmd1.execute("select max(id_contacto) from contacto")
        idconta=0
        for id in cmd:
            idconta=int(id[0])+1'''
        reg=(persona1.nombre,persona1.apellido,persona1.direccion,persona1.fecha)
        cmd.execute("INSERT INTO contacto (nombre_contacto,apellido_contacto,dire_contacto,fecha_contacto)VALUES(?,?,?,?)",reg)
        cone.commit()
        cone.close()
        Label(ventana,text="NUEVO CONTACTO AGREGADO").place(x=250,y=230)
    except ValueError as e:
        print("error :",e)
        cone.commit()
        cone.close()
    
def buscar():
    try:
        cone=sqlite3.connect("contacto.db3")
        cmd=cone.cursor()
        busquedad=busca.get()
        cmd.execute("SELECT * FROM contacto WHERE nombre_contacto='"+busquedad+"' ")
        for datos in cmd:
            Label(ventana,text="ID :"+str(datos[0])).place(x=250,y=100)
            Label(ventana,text="NOMBRE :"+datos[1]).place(x=250,y=130)
            Label(ventana,text="APELLIDO :"+datos[2]).place(x=250,y=160)
            Label(ventana,text="DIRECCION :"+datos[3]).place(x=250,y=190)
            Label(ventana,text="FECHA :"+datos[4]).place(x=250,y=220)
        cone.commit()
        cone.close()
        Label(ventana,text="BUSQUEDAD ENCONTRADA").place(x=250,y=230)
    except ValueError as e:
        print("ERROR :",e)
    
def eliminar():
    try:
        cone=sqlite3.connect("contacto.db3")
        cmd=cone.cursor()
        cmd.execute("delete from contacto where nombre_contacto='"+nomelim.get()+"' and apellido_contacto='"+apeelim.get()+ "'")
        cone.commit()
        cone.close()
        Label(ventana,text="BUSQUEDAD ENCONTRADA").place(x=250,y=230)
    except ValueError as e:
        print("ERROR :",e)
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
ventana.geometry("450x300")
lblnombre=Label(ventana,text="NOMBRE").place(x=10,y=10)#ZONA DE LOS LABELS Y TEXTBOX PARA LA ENTRADA DE VALORES
nombre=StringVar()
txtnombre=Entry(ventana,textvariable=nombre).place(x=100,y=10)
lblapellido=Label(ventana,text="APELLIDO").place(x=10,y=40)
apellido=StringVar()
txtapellido=Entry(ventana,textvariable=apellido).place(x=100,y=40)
lbldire=Label(ventana,text="DIRECCION").place(x=10,y=90)
direccion=StringVar()
txtdire=Entry(ventana,textvariable=direccion).place(x=100,y=90)
lblfecha=Label(ventana,text="FECHA").place(x=10,y=140)
fecha=StringVar()
txtfecha=Entry(ventana,textvariable=fecha).place(x=100,y=140)#FIN DE LA ZONA DE LABELS Y TEXTBOXES
btnnuevo=Button(ventana,text="NUEVO CONTACTO",command=ingresar).place(x=250,y=10)
btnbuscar=Button(ventana,text="BUSCAR CONTACTO",command=buscar).place(x=250,y=40)
btneliminar=Button(ventana,text="ELIMINAR CONTACTO",command=eliminar).place(x=250,y=70)
lblbuscar=Label(ventana,text="BUSQUEDAD POR NOMBRE DE CONTACTO").place(x=10,y=200)
busca=StringVar()
textbuscar=Entry(ventana,textvariable=busca).place(x=70,y=220)
lbleliminar=Label(ventana,text="INDIQUE NOMBRE Y EL APELLIDO DEL CONTACTO A ELIMINAR").place(x=10,y=250)
nomelim=StringVar()
txteleminom=Entry(ventana,textvariable=nomelim).place(x=10,y=270)
apeelim=StringVar()
txteleminape=Entry(ventana,textvariable=apeelim).place(x=150,y=270)
ventana.mainloop()
