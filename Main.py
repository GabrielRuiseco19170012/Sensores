from DHT import DHT
from Sensors import Sensors
from File import File
from MySQL import *
from MongoDB import *
import sys

newSQL = MySQL()
newMongo = MongoDB()
newSQL.Conexion()
newMongo.mongoConexion()

sensors = Sensors()
sensorList = sensors.getAllInstance()
print(sensorList)
sensorList.returnData()
