# 3.- INSETAR REGISTROS DESDE PYTHON A MYSQL --SENTENCIA UPDATE--

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='admin',
    database='personas_db'
)
