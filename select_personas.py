# 1.- SELECCIONAR REGISTROS DESDE PYTHON A MYSQL --SENTENCIA SELECT--

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='admin',
    database='personas_db'
)

# ejecutamos la sencia select
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()  # metodo que nos devuelve todo los registro de la sentencia
for persona in resultado:
    print(persona)

# Cerramos los recursos
cursor.close()
personas_db.close()
