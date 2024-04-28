import pymongo
import pymongo.errors
from AUsuario import AUsuario

class Usuario_persistencia():
    uri = "mongodb+srv://Angel:Angel@cluster0.rvcmuq8.mongodb.net/"
    
    def guarda_usuario(self, usuario: AUsuario) -> AUsuario:
        con = self.conectar_usuario()
        db = con.miBaseDeDatos
        col = db.Usuarios

        guardado = col.insert_one(usuario.to_dict())
        return guardado.asknowledged()

    
    def muestra_usuario(self,valor) -> AUsuario:
        pass

    def update_usuario(self,AUsuario,valor) -> AUsuario:
        pass
    
    def delete_usuario(self,valor) -> AUsuario:
        pass

    def conectar_usuario(self):
        client = pymongo.MongoClient(self.uri)
        return client
    
