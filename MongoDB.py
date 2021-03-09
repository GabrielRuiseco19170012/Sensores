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

    def insertDatosSensor(self, data):
        try:
            self.mydb = self.cliente['RaspberryData']
            self.tabla = self.mydb['Sensors']
            self.datosIns = self.tabla.insert_one(data)
            return "Datos del Sensor insertados a MongoDB"
        except:
            return "No se insertado"
