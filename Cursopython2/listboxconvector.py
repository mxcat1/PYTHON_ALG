'''
Created on 7 jul. 2016

@author: Mxcatv
'''
from Tkinter import *
import Tkinter
import tkMessageBox
import pymssql
from _sqlite3 import Cursor

  

v1=Tk()
def listar():
    n=0
    con=pymssql.connect('localhost:1433','sa','mxcat','BANANITOS')
    cursor=con.cursor()
    cursor.execute('SELECT NOM_CAT FROM CATEGORIA')
    row=cursor.fetchone()
    print str("hola mundo")
    while row:
        print str(row[0])
        ltb1.insert(n,row[0])
        n=n+1
        row=cursor.fetchone()
        


ltb1=Listbox(v1)
btn1=Button(v1,text="lista",command=listar())
btn1.pack()
ltb1.pack()
    
v1.mainloop()
