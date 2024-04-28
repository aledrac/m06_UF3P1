import pymongo
import pymongo.errors

class iUsuario_persistencia():
    uri = "mongodb+srv://Angel:Angel@cluster0.rvcmuq8.mongodb.net/"
    
    def __init__(self, name:str, apellido:str, mail:str, pwd:str) -> None:
        self._name = name
        self._apellido = apellido
        self._mail = mail
        self._pwd = pwd
        #usuario py constructor con metodo todic
        #iUsuario_persistencia metodos vacios
        #Persistencia_mongo_usuario.py metodos desarrollados
        #Test apunta a la persistencia
    
    #region ///////Region de modulos funcionales
    def guarda_usuario(self, lista) -> int:
        try:
            con = self.conectar_usuario()
            db = con.miBaseDeDatos
            col = db.Usuarios

            if not lista:
                print("No has insertado nada")
                return 0
            elif len(lista) == 1:
                user1 = iUsuario_persistencia(lista[0]["name"],lista[0]["apellido"],lista[0]["mail"],lista[0]["pwd"])

                resultado = col.insert_one(user1)
                inserted_count = resultado.inserted_count
            else:
                usuarios_insertar = []
                for a in lista:
                    nuevo_usuario = iUsuario_persistencia(a["name"],a["apellido"],a["mail"],a["pwd"])
                    usuarios_insertar.append(nuevo_usuario.__dict__)
                
                resultado = col.insert_many(usuarios_insertar)
                
                inserted_count = len(lista)
                
            return inserted_count
        except pymongo.errors.ConnectionFailure:
            print("Error: No se ha podido agregar un usuario a la bdd")
            return 0
        finally:
            con.close()



    def delete_usuario(self,valor) -> dict: #BIEN
        try:
            con = self.conectar_usuario()
            db = con.miBaseDeDatos
            col = db.Usuarios
            
            userEliminado = col.find_one({"$or":[{"name":valor},{"apellido":valor},{"mail":valor},{"pwd":valor}]})
            col.delete_one({"$or":[{"name":valor},{"apellido":valor},{"mail":valor},{"pwd":valor}]})
            
            con.close()
            return userEliminado
        except pymongo.errors.ConnectionFailure:
            print("Error: No se ha podido eliminar un registro de usuario de la bdd")
            return None

    def update_usuario(self,nuevoUser,valor) -> dict:
        try:
            con = self.conectar_usuario()
            db = con.miBaseDeDatos
            col = db.Usuarios

            usuarioExiste = col.find_one({"$or":[{"name":valor},{"apellido":valor},{"mail":valor},{"pwd":valor}]})
            if usuarioExiste:
                col.update_one({"_id":usuarioExiste["_id"]},{"$set":nuevoUser})
                return usuarioExiste["_id"]
            else:
                print("[Not found] No se ha encontrado el usuario con el valor "+valor)
                return None
        except pymongo.errors.ConnectionFailure as e:
            print("Error: No ha sido posible ctualizar el usuario en la bdd.")

    def muestra_usuario(self,valor):
        try:
            con = self.conectar_usuario()
            db = con.miBaseDeDatos
            col = db.Usuarios
            usuarioExiste = col.find({"$or":[{"name":valor},{"apellido":valor},{"mail":valor},{"pwd":valor}]})
            if usuarioExiste:
                print("Id: ",usuarioExiste["name"])
                print("Nombre: ",usuarioExiste["name"].return_value)
                print("Apellido: ",usuarioExiste.get('apellido'))
                print("E-Mail: ",usuarioExiste["mail"].return_value)
                print("Contraseña: ",usuarioExiste["pwd"])
                return usuarioExiste
            else:
                return None
        except pymongo.errors.ConnectionFailure:
            print("Error: No se ha podido mostrar el usuario")
    #endregion

    #region //////Region de modulos opcionales

    def conectar_usuario(self):
        client = pymongo.MongoClient(self.uri)
        return client

    #endregion
    
    #region ///////Region getters & setters

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name:str):
        self._name = name
        
    @property
    def apellido(self) -> str:
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido:str):
        self._apellido = apellido
        
    @property
    def mail(self) -> str:
        return self._mail
    
    @mail.setter
    def mail(self, mail:str):
        self._mail = mail
        
    @property
    def pwd(self) -> str:
        return self._pwd
    
    @pwd.setter
    def pwd(self, pwd:str):
        self._pwd = pwd
    
    #endregion

