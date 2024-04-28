

class AUsuario():
    
    def __init__(self, name:str, apellido:str, mail:str, pwd:str) -> None:
        self._name = name
        self._apellido = apellido
        self._mail = mail
        self._pwd = pwd
    
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
    
    def to_dict(self):
        return {"name": self.name, "apellido": self.apellido, "mail": self.mail, "pwd": self.pwd}