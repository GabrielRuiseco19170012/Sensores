# from DHT import *
# from HCR import *
# from PIR import *
from Sensors import Sensors
from File import File

try:
    file = File.readData()
except Exception as e:
    file = []

dht = Sensors.getListDHT()
hcr = Sensors.getListHCR()
pir = Sensors.getListPIR()

# newDHT = DHT(4)
# newHCR = HCR(17, 18)
# newPIR = PIR(24)

try:
    while True:
        for x in dht:
            x.leerTemperatura()
            x.guardarDatosSQL()
            x.guardarDatosMongo()
            file.append(x.retornarDatos())
            print(x.retornarDatos())

        for x in hcr:
            x.leerPrescencia()
            x.guardarDatosPIRSQL()
            x.guardarDatosPIRMongo()
            file.append(x.retornarDatos())
            print(x.retornarDatos())

        for x in pir:
            x.leerDistancia()
            x.guardarDatosSQL()
            x.guardarDatosMongo()
            file.append(x.retornarDatos())
            print(x.retornarDatos())

        File.saveData(file)
except KeyboardInterrupt:
    print("adios")
