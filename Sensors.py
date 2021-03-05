from DHT import *
from HCR import *
from PIR import *
from DataList import DataList

dht = DataList()
hcr = DataList()
pir = DataList()

DHT1 = DHT(4)
HCR1 = HCR(17, 18)
PIR1 = PIR(24)

dht.setDataList([DHT1])
hcr.setDataList([HCR1])
pir.setDataList([PIR1])


class Sensors:

    @staticmethod
    def getListDHT():
        return DHT

    @staticmethod
    def getListHCR():
        return HCR

    @staticmethod
    def getListPIR():
        return PIR

    @staticmethod
    def addDHT(pin):
        nuevo = DHT(pin)
        dht.addData(nuevo)

    @staticmethod
    def addHCR(trig, echo):
        nuevo = HCR(trig, echo)
        hcr.addData(nuevo)

    @staticmethod
    def addPIR(pin):
        nuevo = PIR(pin)
        pir.addData(nuevo)
