# 4.- ELIMINAR REGISTROS DESDE PYTHON A MYSQL --SENTENCIA UPDATE--

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='admin',
    database='personas_db'
)
# Ejecutamos la sencia delete
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (7,)  # Para que sea una tupla agremgamos una coma al final
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se a eliminado el registro')
cursor.close()
personas_db.close()
