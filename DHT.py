from MySQL import *
from MongoDB import *
import Adafruit_DHT
import time
from datetime import datetime
newSQL = MySQL()
newMongo = MongoDB()
class DHT:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT11
        self.DHT11_pin = 4
        self.datos = (0,0,"")
        self.temperature = 0
        self.humidity = 0
        self.fecha = ""
        newSQL.Conexion()
        newMongo.mongoConexion()
        
    def leerTemperatura(self):
        self.humidity, self.temperature = Adafruit_DHT.read(self.sensor, self.DHT11_pin)
        if self.humidity is not None and self.temperature is not None:
            #print("Temperatura:",self.temperature,"|","°C","Humedad:",self.humidity,"%")
            self.ahora = datetime.now()
            self.fecha = self.ahora.strftime("%Y-%m-%d %H:%M:%S")
            self.datos = (self.temperature,self.humidity,self.fecha)
            time.sleep(1)
            
    def guardarDatosSQL(self):
        newSQL.guardarDatos(self.datos)
        
    def retornarDatos(self):
        return self.temperature, self.humidity, self.fecha
    
    def guardarDatosMongo(self):
        newMongo.insertDatosSensor(self.temperature,self.humidity,self.fecha)
    
    
    
    