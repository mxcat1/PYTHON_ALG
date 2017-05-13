'''
Created on 22 de jun. de 2016

@author: Mxcatv
'''
mensaje = input("Escribe el mensaje \n ->")
k = 13
m = input("Escribe D para decifrar o C para cifrar \n ->")
m=m.upper()
l = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
r = ""
mensaje = mensaje.upper()

for s in mensaje:
    if s in l:
        num = l.find(s)
        if m == "C":
            num = num + k
        elif m == "D":
            num = num - k

        if num >=len(l):
            num = num - len(l)
        elif num < 0:
            num = num + len(l)

        r = r+l[num]
    else:
        r = r + s

print(r)