import RPi.GPIO as GPIO
import time
from MySQL import *
from MongoDB import *
from datetime import datetime
newSQL = MySQL()
newMongo = MongoDB()
class PIR:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.IN, GPIO.PUD_DOWN)
        self.estado_anterior = False
        self.estado_actual = False
        self.nuevo_estado = ""
        self.datos = ("","")
        self.fecha = ""
        newSQL.Conexion()
        newMongo.mongoConexion()
        
    def leerPrescencia(self):
        self.estado_previo = self.estado_actual
        self.estado_actual = GPIO.input(24)
        if self.estado_actual != self.estado_previo:
            self.nuevo_estado = "DETECTADO" if self.estado_actual else "NON"
            self.ahora = datetime.now()
            self.fecha = self.ahora.strftime("%Y-%m-%d %H:%M:%S")
            self.datos = (self.nuevo_estado,self.fecha)
            time.sleep(1)
    
    def retornarDatosPIR(self):
        return self.datos
    
    def guardarDatosPIRSQL(self):
        newSQL.guardarDatosPIR(self.datos)
        
    def guardarDatosPIRMongo(self):
        newMongo.insertDatosSensorPIR(self.nuevo_estado, self.fecha)
        