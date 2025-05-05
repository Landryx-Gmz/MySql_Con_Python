# 3.- ACTUALIZMOS REGISTROS DESDE PYTHON A MYSQL --SENTENCIA UPDATE--

import mysql.connector

from insertar_personas import sentencia_sql

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='admin',
    database='personas_db'
)
# Ejecutamos la sencia update
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre =%s, apellido=%s, edad =%s WhERE id=%s'
valores = ('Victoria', 'Flores', 45, 6)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la informacion....')
# Cerramos los recursos
cursor.close()
personas_db.close()
