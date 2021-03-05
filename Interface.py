from DataList import DataList
from File import File

sensors = DataList()


class Interface(object):

    @staticmethod
    def saveFile():
        File.saveData(sensors)

    @staticmethod
    def newSensor(name, sensor):
        sensors.addData(name, sensor)

