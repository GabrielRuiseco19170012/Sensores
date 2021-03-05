import RPi.GPIO as GPIO
import time
from datetime import datetime
from MySQL import *
from MongoDB import *

newSQL = MySQL()
newMongo = MongoDB()


class HCR:
    def __init__(self,trigger,echo):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.GPIO_TRIGGER = trigger
        self.GPIO_ECHO = echo
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        self.StartTime = 0
        self.StopTime = 0
        self.TimeElapsed = 0
        self.distance = 0
        self.fecha = ""
        newSQL.Conexion()
        self.datos = ("", "")
        newMongo.mongoConexion()

    def leerDistancia(self):
        GPIO.output(self.GPIO_TRIGGER, True)

        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        self.StartTime = time.time()
        self.StopTime = time.time()

        while GPIO.input(self.GPIO_ECHO) == 0:
            self.StartTime = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            self.StopTime = time.time()

        self.TimeElapsed = self.StopTime - self.StartTime
        self.distance = (self.TimeElapsed * 34300) / 2
        self.ahora = datetime.now()
        self.fecha = self.ahora.strftime("%Y-%m-%d %H:%M:%S")
        self.datos = (self.distance, self.fecha)

    def retornarDistancia(self):
        return self.distance

    def guardarDatosSQL(self):
        newSQL.guardarDatosHCR(self.datos)

    def guardarDatosMongo(self):
        newMongo.insertDatosSensorHCR(self.distance, self.fecha)
