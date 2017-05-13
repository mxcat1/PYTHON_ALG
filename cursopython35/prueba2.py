'''
Created on 22 de jun. de 2016

@author: Mxcatv
'''
import os,tkinter,tkinter.filedialog
from tkinter import *

c =filedialog

p = r"%s"%(c)

la = []

ld = os.walk(p)

nMU = input("Escribe el nuevo nombre para tus archivos \n ->")
i = 1
nb = []

for root, dirs, files in ld:
    for fh in files:
        (nomFichero,extension) = os.path.splitext(fh)
        la.append(nomFichero+extension)
        nvm = "%s 00%d%s"%(nMU,i,extension)
        i = i+1
        nb.append(nvm)

print(nb)
print(la)
contador = len(la)
for x in range(contador):
    os.rename(os.path.join(p, la[x]),os.path.join(p,nb[x]))
    

        
