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

try:
    file = File.readData()
except Exception as e:
    file = []

sensors = Sensors()
sensorList = sensors.getAllInstance().getDataList()
print(sensorList)
try:
    while True:
        for element in sensorList:
            if (getattr(element,'idName'))[0:3] == 'dht':
                element.leerTemperatura()
                data = element.retornarDatos()
                print(str(data['data']))
                if (data['data']==[None, None]):
                    newSQL.guardarDatos(data)
                    newMongo.insertDatosSensor(data)
                    file.append(data)
                    File.saveData(file)
                else:
                    print('nodata')
            elif (getattr(element,'idName'))[0:3] == 'hcr':
                element.leerDistancia()
                data = element.retornarDistancia()
                print(data['data'])
                if (data['data']!=[None, None]):
                    newSQL.guardarDatos(data)
                    newMongo.insertDatosSensor(data)
                    file.append(data)
                    File.saveData(file)
                else:
                    print('nodata')
            elif (getattr(element,'idName'))[0:3] == 'pir':
                element.leerPrescencia()
                data = element.retornarDatosPIR()
                print(data['data'])
                if (data['data']!=[None, None]):
                    newSQL.guardarDatos(data)
                    newMongo.insertDatosSensor(data)
                    file.append(data)
                    File.saveData(file)
                else:
                    print('nodata')
            else:
                print('Error')
except KeyboardInterrupt:
    print("adios")
    sys.exit()
