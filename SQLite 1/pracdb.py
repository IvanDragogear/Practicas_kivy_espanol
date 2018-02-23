# -*- coding: utf-8 -*-
import sqlite3
import os

# Ubicación del archivo
APP_PATH = os.getcwd()
DB_PATH = APP_PATH+'/my_database.db'

# CONECTARSE a base de datos o CREAR base de datos
con = sqlite3.connect(DB_PATH)

# Crear cursor 
cursor = con.cursor()

# Crear una tabla
try:
    cursor.execute("""
        CREATE TABLE PACIENTES(
        ID          INT     PRIMARY KEY NOT NULL,
        NOMBRE      TEXT                NOT NULL,
        EDAD        INT,
        ENFERMO     BIT                 NOT NULL
        )""")
except Exception as e:
    print e

# Insetar datos
try:
    cursor.execute("""
        INSERT INTO PACIENTES(ID, NOMBRE, EDAD, ENFERMO)
        VALUES(1, 'Ivan', 25, 0)
        """)
        
    cursor.execute("""
        INSERT INTO PACIENTES(ID, NOMBRE, ENFERMO)
        VALUES(2, 'Juan', 1)
        """)
        
    cursor.execute("""
        INSERT INTO PACIENTES(ID, NOMBRE, EDAD, ENFERMO)
        VALUES(3, 'Jhon', 18, 1)
        """)
    con.commit()# Para que el cambio se ejecute
except Exception as e:
    print e
    
# Seleccionar valores de una tabla
cursor.execute("""
    SELECT NOMBRE, EDAD, ENFERMO FROM PACIENTES
    """)
    
# Consultar el cursor
for i in cursor:
    print 'Paciente', i
print '.........................'

# Seleccionar un dato por su ID
cursor.execute("""
    SELECT ID, NOMBRE, EDAD, ENFERMO FROM PACIENTES WHERE ID=3
    """)

# Consultar el cursor
for i in cursor:
    print 'ID:', i[0]
    print 'Nombre:', i[1]
    print 'Edad:', i[2]
    print 'Enfermo:', i[3]
print '_____________________'

# Actualizar datos 
cursor.execute("""
    UPDATE PACIENTES SET EDAD=30 WHERE NOMBRE='Ivan'
    """)
con.commit() # Para que el cambio se ejecute

# Actualizar datos
cursor.execute("""
    DELETE FROM PACIENTES WHERE ID=3
    """)
con.commit()

con.close()
