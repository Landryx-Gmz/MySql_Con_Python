# 4.- ELIMINAR REGISTROS DESDE PYTHON A MYSQL --SENTENCIA UPDATE--

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='admin',
    database='personas_db'
)
# Ejecutamos la sencia DELETE
cursor = personas_db.cursor()
# Objeto de sentencia DELETE
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
# Proporcionamos el valor en el mismo orden
valores = (7,)  # Para que sea una tupla agremgamos una coma al final
# Ejecutamos la sentencia con el objeto de cursor y el metodo execute (senstencia,valores)
cursor.execute(sentencia_sql, valores)
# Guardamos en la BD
personas_db.commit()
print('Se a eliminado el registro')
# Cerramos los recursos
cursor.close()
personas_db.close()
