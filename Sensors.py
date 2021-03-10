from DHT import *
from HCR import *
from PIR import *
from DataList import DataList

sensorList = [
    {'name': 'dht1', 'pin': [2]},
    {'name': 'dht2', 'pin': [3]},
    {'name': 'dht3', 'pin': [4]},
    {'name': 'hcr1', 'pin': [17, 11]},
    {'name': 'hcr2', 'pin': [27, 5]},
    {'name': 'pir1', 'pin': [22]},
    {'name': 'pir2', 'pin': [10]},
    {'name': 'pir3', 'pin': [9]},
]


class Sensors:

    def __init__(self):
        self.instancesList = DataList()
        self.createInstances()

    def createInstances(self):
        for o in sensorList:
            if self.instancesList.getData(None, o['name']) is None:
                if o['name'][0:3] == 'dht':
                    instance = DHT(o['name'], o['pin'][0])
                    self.instancesList.addData(instance)
                elif o['name'][0:3] == 'hcr':
                    instance = HCR(o['name'], o['pin'][0], o['pin'][1])
                    self.instancesList.addData(instance)
                elif o['name'][0:3] == 'pir':
                    instance = PIR(o['name'], o['pin'][0])
                    self.instancesList.addData(instance)
                else:
                    print('error al generar instancia')

    def getOneInstance(self, name):
        return self.instancesList.getData(name)

    def getAllInstance(self):
        return self.instancesList
