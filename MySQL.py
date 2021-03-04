from mysql.connector.connection import MySQLConnection
from datetime import datetime
class MySQL:
    def __init__(self):
        self.host="localhost"
        self.user="admin"
        self.password="12345"
        self.database="examen"

    def Conexion(self):
        self.mydb = MySQLConnection(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return "Conexion a MySQL exitosa"
#DHT----------------------------------------------------------------
    def guardarDatos(self,datos):
        self.sql = "insert into SensorDHT (temperatura, humedad, fechaLectura) values (%s, %s, %s)"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql,datos)
        self.mydb.commit()
#PIR----------------------------------------------------------------
    def guardarDatosPIR(self,estado):
        self.sql = "insert into SensorPIR (estado,fechaLectura) values (%s,%s)"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql,estado)
        self.mydb.commit()
#HCR----------------------------------------------------------------
    def guardarDatosHCR(self,distancia):
        self.sql = "insert into SensorHCR (distancia,fechaLectura) values (%s,%s)"
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(self.sql,distancia)
        self.mydb.commit()
        
        
        
        