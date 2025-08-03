# 3.- ACTUALIZMOS REGISTROS DESDE PYTHON A MYSQL --SENTENCIA UPDATE--

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='admin',
    database='personas_db'
)
# Ejecutamos la sencia update
cursor = personas_db.cursor()
# Objeto de sentencia Update
sentencia_sql = 'UPDATE personas SET nombre =%s, apellido=%s, edad =%s WhERE id=%s'
# Agregamos los valores en el mismo orden
valores = ('Victoria', 'Flores', 47, 6)
# Ejecutamos la sentencia con el objeto de cursor y el metodo execute (senstencia,valores)
cursor.execute(sentencia_sql, valores)
# guardamos los cambios en la BD
personas_db.commit()
print('Se ha modificado la informacion....')
# Cerramos los recursos
cursor.close()
personas_db.close()
