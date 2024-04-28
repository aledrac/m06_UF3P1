from typing import List
import pymongo
import pymongo.errors
from AUsuario import AUsuario

class Usuario_persistencia():
    uri = "mongodb+srv://Angel:Angel@cluster0.rvcmuq8.mongodb.net/"
    
    def guarda_usuario(self, usuario: AUsuario) -> bool:#XX
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        userDiccionario = usuario.to_dict()
        guardado = col.insert_one(userDiccionario)
        return guardado.acknowledged

    
    def muestra_usuario(self,valor: str) -> AUsuario: #XX
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        return col.find_one(valor)

    def update_usuario(self,user:AUsuario,nombre:str) -> int: #
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        filtro = {"nombre":nombre}
        update = { "$set":user.to_dict() }
        mod = col.update_many(filtro,update)

        return mod.modified_count
    
    def delete_usuario(self,valor:str) -> AUsuario:
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        deleted = col.delete_one(valor)
        return deleted.deleted_count()

    def conectar_usuario(self):
        client = pymongo.MongoClient(self.uri)
        return client
    
