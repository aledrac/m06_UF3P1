class Agenda:
    def __init__(self, name:str, listaEvents: list, listaUserS: list) -> None:
        self.name=name
        self.listaEvents=listaEvents
        self.listaUserS=listaUserS
        
    @property
    def name(self) -> str:
        return self.name
    
    @name.setter
    def name(self, name: str) -> None:
        self.name = name
        
    
    @property
    def listaEvents(self) -> list:
        return self.listaEvents
    
    @listaEvents.setter
    def listaEvents(self, listaEvents: list) -> None:
        self.listaEvents = listaEvents
    
    
    @property
    def listaUserS(self) -> list:
        return self.listaUserS
    
    @listaUserS.setter
    def listaUserS(self, listaUserS: list) -> None:
        self.listaUserS = listaUserS
    
    
    def toList(self, evento) -> list:
        self.agenda.append(evento)
    