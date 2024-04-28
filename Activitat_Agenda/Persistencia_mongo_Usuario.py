from typing import List
from iUsuario_persistencia import IUsuarioPersistencia
import pymongo 
from Usuario import Usuario

class Persistencia_mongo_Usuario(IUsuarioPersistencia):
    pwd = "david"
    user = "david"
    cluster = "cluster0.rvcmuq8"
    uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
    def __init__(self, uri) :
        self.conection = pymongo.MongoClient(uri)
        self.db = self.conection.agendadb
        self.coleccio = self.db.usuario
    
    
    def read_user(self) -> List[Usuario]:
        return list(self.coleccio.find())
    
    def read_user_valor(self, valor):
        return list(self.coleccio.find(valor))
    
    def save_user(self, user: Usuario):
        user_dict = user.to_dict()
        ins = self.coleccio.insert_one(user_dict)
        return ins.asknowledged()

    def udpate_user(self, name, user: Usuario):
        filtro = { "name": name }  
        actualizacion = { "$set": user.to_dict() }  
        mod = self.coleccio.update_many(filtro, actualizacion)
        return mod.modified_count()
    
    
    def delete_user(self, valor):
        deleted = self.coleccio.delete_one(valor)
        return deleted.deleted_count()
    