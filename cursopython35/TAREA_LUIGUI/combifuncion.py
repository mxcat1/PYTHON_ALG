'''
Created on 8 may. 2017

@author: MAXCAT
'''

def factorial(n1):
    nun1=float(n1)
    if(nun1==0):
        return 1
    else:
        return nun1*factorial(nun1-1)
    

def cobinatoria(n1,n2):
    nun1=float(n1)
    nun2=float(n2)
    resultado=factorial(nun1)/(factorial(nun2)*factorial(nun1-nun2))
    return resultado
