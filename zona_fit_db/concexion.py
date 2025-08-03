# 1
from mysql.connector import pooling
from mysql.connector import Error  # importamos la clase de error para mysql


class Conexion:
    DATABASE = 'zona_fit_db'
    USARNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # se creal el objeto pool si es none
            try:
                # Creacion del objeto de pool
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USARNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obterner pool {e}')
        # Si el objeto pool no es none
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        # Retornamos un objeto del tipo pool un objeto de conexion
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):  # Recibimos el objeto conexion que ya hemos obtenido
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se a liberado el objeto: {conexion1}')
