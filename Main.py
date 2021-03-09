from DHT import DHT
from Sensors import Sensors
from File import File
from MySQL import *
from MongoDB import *

newSQL = MySQL()
newMongo = MongoDB()
newSQL.Conexion()
newMongo.mongoConexion()

try:
    file = File.readData()
except Exception as e:
    file = []

sensors = Sensors()
sensorList = sensors.getAllInstance()

try:
    while True:
        for element in sensorList:
            if element['name'][0:3] == 'dht':
                element.leerTemperatura()
                data = element.retornarDatos()
                newSQL.guardarDatos(data)
                newMongo.insertDatosSensor(data)
                file.append(data)
                File.saveData(file)
            elif element['name'][0:3] == 'hcr':
                element.leerDistancia()
                data = element.retornarDistancia()
                newSQL.guardarDatos(data)
                newMongo.insertDatosSensor(data)
                file.append(data)
                File.saveData(file)
            elif element['name'][0:3] == 'pir':
                element.leerPrescencia()
                data = element.retornarDatosPIR()
                newSQL.guardarDatos(data)
                newMongo.insertDatosSensor(data)
                file.append(data)
                File.saveData(file)
            else:
                print('Error')
except KeyboardInterrupt:
    print("adios")
