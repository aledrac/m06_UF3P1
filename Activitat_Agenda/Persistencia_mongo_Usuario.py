from typing import List
import pymongo
import pymongo.errors
from Usuario import Usuario

class Usuario_persistencia():
    uri = "mongodb+srv://Angel:Angel@cluster0.rvcmuq8.mongodb.net/"
    
    def guarda_usuario(self, usuario: Usuario) -> bool:#XX
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        userDiccionario = usuario.to_dict()
        guardado = col.insert_one(userDiccionario)
        return guardado.acknowledged

    
    def muestra_usuario(self,valor: str) -> dict: #XX
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        user_dict = col.find_one({"nombre": valor})

        return user_dict

    def update_usuario(self,user:Usuario,nombre:str) -> int: #XX
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        filtro = {"nombre":nombre}
        update = { "$set":user.to_dict() }
        mod = col.update_many(filtro,update)

        return mod.modified_count
    
    def delete_usuario(self,valor:str) -> Usuario:
        con = self.conectar_usuario()
        db = con.agendadb
        col = db.usuario

        deleted = col.delete_one(valor)
        return deleted.deleted_count()

    def conectar_usuario(self):
        client = pymongo.MongoClient(self.uri)
        return client
    
