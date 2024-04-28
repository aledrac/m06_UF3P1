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
        return list(self.conection.find())
    
    def read_user_valor(self, valor) -> Usuario:
        return self.conection.find(valor)
    
    def save_user(self, user: Usuario):
        user_dict = user.to_dict()
        ins = self.conection.insert_one(user_dict)
        return ins.asknowledged()

    def udpate_user(self, name, user: Usuario):
        filtro = { "name": name }  
        actualizacion = { "$set": user.to_dict() }  
        mod = self.conection.update_many(filtro, actualizacion)
        return mod.modified_count()
    
    
    def delete_user(self, valor):
        deleted = self.conection.delete_one(valor)
        return deleted.deleted_count()
    