import psycopg2
from psycopg2 import pool
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extensions import connection
config = {
    'HOST': 'localhost',
    'PORT': '5432',
    'USER': 'postgres',
    'PASS': 'admin',
    'DB':'examen'
}


class Connection: 
    _host= config['HOST']
    _port= config['PORT']
    _db= config['DB']
    _user= config['USER']
    _password= config['PASS']
    _conn = None
    _pool = None
    _min_conn = 1
    _max_conn = 5

    def __init__(self):
        pass

    @classmethod
    def obtenerPool(cls) :
        if cls._pool is None:
           cls._pool = pool.SimpleConnectionPool(cls._min_conn, cls._max_conn,user=cls._user, password=cls._password,host=cls._host, port=cls._port, database=cls._db)
        return cls._pool

    @classmethod
    def getConnection(cls):
        conn = cls.obtenerPool().getconn()
        return conn

    @classmethod
    def putConnection(cls, conexion: connection):
        cls.obtenerPool().putconn(conexion)

    @classmethod
    def closeAll(cls):
        cls.obtenerPool().closeAll()  
