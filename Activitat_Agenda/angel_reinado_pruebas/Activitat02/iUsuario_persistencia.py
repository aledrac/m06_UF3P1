import pymongo

class iUsuario_persistencia():
    uri = "mongodb+srv://Angel:Angel@cluster0.rvcmuq8.mongodb.net/"
    
    def __init__(self, name:str, apellido:str, mail:str, pwd:str, uri) -> None:
        self.name = name
        self.apellido = apellido
        self.mail = mail
        self.pwd = pwd
        
    
    #region ///////Region de modulos funcionales
    def guarda_usuario(self,lista) -> int:
        con = self.conectar_usuario()
        clean = True
        if len(lista) <= 0:
            print("Cagadon no has insertado nada")
            clean = False
        elif len(lista) == 1:
            con.insertone()
        else:
            con.insertmany()

        con.close

        if clean == True:
            return con.inserted_count
        else:
            return 0



    def delete_usuario(self,valor) -> str:
        
        

        return "objeto id"



    def update_usuario(self,user):
        pass

    def muestra_usuario(self,user):
        pass
    #endregion

    #region //////Region de modulos opcionales

    def conectar_usuario(self):
        client = pymongo.MongoClient(self.uri)
        return client

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