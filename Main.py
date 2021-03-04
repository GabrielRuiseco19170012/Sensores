from DHT import *
from HCR import *
from PIR import *
newDHT = DHT()
newHCR = HCR()
newPIR = PIR()
try:
    while True:
        newDHT.leerTemperatura()
        newDHT.guardarDatosSQL()
        newDHT.guardarDatosMongo()
        print(newDHT.retornarDatos())
        newPIR.leerPrescencia()
        newPIR.guardarDatosPIRSQL()
        newPIR.guardarDatosPIRMongo()
        print(newPIR.retornarDatosPIR())
        newHCR.leerDistancia()
        newHCR.guardarDatosSQL()
        newHCR.guardarDatosMongo()
        print("Distancia:",newHCR.retornarDistancia(),"cm")
except KeyboardInterrupt:
    print("adios")


