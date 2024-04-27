class Usuario():
    def __init__(self, name:str, apellido:str, mail:str, pwd:str) -> None:
        self.name = name
        self.apellido = apellido
        self.mail = mail
        self.pwd = pwd
    

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
        
    def to_dict(self):
        return {"name": self.name, "apellido": self.apellido, "mail": self.mail, "pwd": self.pwd}
        
    
