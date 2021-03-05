import pymongo


class MongoDB:
    def __init__(self):
        pass

    def mongoConexion(self):
        self.Mongo_URI = "mongodb+srv://user:user@cluster0.0fjcd.mongodb.net/test"
        # self.Mongo_URI="mongodb://"+self.Mongo_Host+":"+self.Mongo_Port+"/"
        try:
            # self.cliente = pymongo.MongoClient(self.Mongo_URI)
            self.cliente = pymongo.MongoClient(self.Mongo_URI)
            self.cliente.server_info()
            return "Conexion a MongoDB Exitosa"
        except pymongo.errors.ConnectionFailure as errorConexion:
            return "No se pudo realizar la conexion a MongoDB " + errorConexion

    def insertDatosSensor(self, temperatura, humedad, fecha):
        try:
            self.mydb = self.cliente['Sensores']
            self.tabla = self.mydb['SensorDHT']
            self.datos = {"temperatura": temperatura, "humedad": humedad, "fecha": fecha}
            self.datosIns = self.tabla.insert_one(self.datos)
            return "Datos del Sensor DHT insertados a MongoDB"
        except:
            return "No se inserto nada"

    def insertDatosSensorPIR(self, estado, fecha):
        try:
            self.mydb = self.cliente['Sensores']
            self.tabla = self.mydb['SensorPIR']
            self.datos = {"estado": estado, "fecha": fecha}
            self.datosIns = self.tabla.insert_one(self.datos)
            return "Datos del Sensor PIR insertados a MongoDB"
        except:
            return "No se inserto nada"

    def insertDatosSensorHCR(self, distancia, fecha):
        try:
            self.mydb = self.cliente['Sensores']
            self.tabla = self.mydb['SensorHCR']
            self.datos = {"distancia": distancia, "fecha": fecha}
            self.datosIns = self.tabla.insert_one(self.datos)
            return "Datos del sensor HCR insertados a MongoDB"
        except:
            return "No se inserto nada"
