'''
Created on 19 may. 2017

@author: MAXCAT
'''
# CREAR UN DIRECTORIO DE CONTACTOS:
# INSERCION (QUE EL NOMBRE DE CONTACTO NO SE REPITA),
# BUSQUEDA, ELIMINACION


class Persona:
    fecha = [0, 0, 0]
    Nombre = ""
    Apellido = ""
    Direccion = ""

    def __init__(self):
        print ("Constructor")

    def ingreso(self, x, y, z, a, b, c):
        self.Nombre = x
        self.Apellido = y
        self.Direccion = z
        self.fecha = [a, b, c]


lista = []
# ObjPersona = Persona()
while True:
    lista.append(Persona())
    lista[0].ingreso("Luigi", "Colque", "Arequipa", 2, 2, 1990)
    lista.append(Persona())
    lista[1].ingreso("Elena", "Pareja", "Monterrey", 1, 1, 1996)
    print (lista[0].Nombre)
    print (lista[0].fecha)
    print (lista[1].Nombre)
    print (lista[1].fecha)
    break
