'''
Created on 21 de jun. de 2016

@author: Mxcatv
'''
from Tkinter import *


f=Tk()
f.config(bg='black')
f.geometry('250x200')
h=Label(f, text='hola').pack()
j=Button(f,text="botond")
j.pack()

h=Toplevel(f)
f.mainloop()
