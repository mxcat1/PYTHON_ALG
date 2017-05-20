'''
Created on 19 may. 2017

@author: MAXCAT
'''
class persona():
    fecha=[0,0,0]
    nombre=""
    apellido=""
    direccion=""
    
    def __init__(self,nombre,fecha,apellido,direccion):
        self.apellido=apellido
        self.nombre=nombre
        self.fecha=fecha
        self.direccion=direccion
        
        
        
    def ingreso(self,n,a,d,dd,mm,aa):
        self.nombre=n
        self.apellido=a
        self.direccion=d
        self.fecha=[dd,mm,aa]
        
