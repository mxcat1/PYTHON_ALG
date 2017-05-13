'''
Created on 27 jun. 2016

@author: Mxcatv
'''
import pymssql
from _sqlite3 import Cursor


con=pymssql.connect('localhost:1433','sa','mxcat','BANANITOS')
cursor=con.cursor()
cursor.execute('SELECT NOM_CAT FROM CATEGORIA')
row=cursor.fetchone()
while row:
    print str(row[0])
    row=cursor.fetchone()