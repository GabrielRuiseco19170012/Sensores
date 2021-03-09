from mysql.connector.connection import MySQLConnection
from datetime import datetime


class MySQL:
    def __init__(self):
        self.host = "localhost"
        self.user = "admin"
        self.password = "12345"
        self.database = "examen"

    def Conexion(self):
        self.mydb = MySQLConnection(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return "Conexion a MySQL exitosa"

    # DHT----------------------------------------------------------------
    def guardarDatos(self, data):
        self.sql = "insert into Sensors (IDName, Data, Type) values (%s, %s, %s)"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql, data['name'], data['data'], data['type'])
        self.mydb.commit()
