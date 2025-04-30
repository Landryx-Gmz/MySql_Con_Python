# 2.- INSETAR REGISTROS DESDE PYTHON A MYSQL --SENTENCIA INSERT--

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='admin',
    database='personas_db'
)

# EJECUTAMOS LA SENTECNIA INSERT
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)'
