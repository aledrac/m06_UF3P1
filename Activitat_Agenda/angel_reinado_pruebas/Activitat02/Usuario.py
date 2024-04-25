import pymongo

class Usuario():
    uri=""

    def __init__(self, name:str, apellido:str, mail:str, pwd:str) -> None:
        self.name = name
        self.apellido = apellido
        self.mail = mail
        self.pwd = pwd
        self.uri = "mongodb+srv://Angel:Angel@cluster0.rvcmuq8.mongodb.net/"
    
    #region ///////Region de modulos funcionales
    def guarda_usuario(self,usuariosList) -> bool:
        #Operacion principal
        client = pymongo.MongoClient(self.uri)
        collection = client.Usuarios
        collection.insert_many(usuariosList)
        #Operacion existe y devuelve
        return False

    def delete_usuario(self):
        pass

    def update_usuario(self):
        pass

    def muestra_usuario(self):
        pass
    #endregion
    
    #region ///////Region getters & setters

    @property
    def name(self) -> str:
        return self.name
    
    @name.setter
    def name(self, name:str):
        self.name = name
        
    @property
    def apellido(self) -> str:
        return self.apellido
    
    @apellido.setter
    def apellido(self, apellido:str):
        self.apellido = apellido
        
    @property
    def mail(self) -> str:
        return self.mail
    
    @mail.setter
    def mail(self, mail:str):
        self.mail = mail
        
    @property
    def pwd(self) -> str:
        return self.pwd
    
    @pwd.setter
    def pwd(self, pwd:str):
        self.pwd = pwd
    
    #endregion