from typing import List
from iUsuario_persistencia import IUsuarioPersistencia
import pymongo 
from Usuario import Usuario

class Persistencia_mongo_Usuario(IUsuarioPersistencia):
    pwd = "Angel"
    user = "Angel"
    cluster = "cluster0.rvcmuq8"
    uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
    conection = pymongo.MongoClient(uri)
    
    def read_user(self, r) -> List[Usuario]:
        return self.conection.find()
    
    def read_user_valor(self, valor) -> Usuario:
        return self.conection.find(valor)
    