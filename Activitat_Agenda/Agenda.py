class Agenda:
    def __init__(self, name:str, listaEvents: list, listaUserS: list) -> None:
        self._name = name
        self._listaEvents = listaEvents
        self._listaUserS = listaUserS
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
        
    
    @property
    def listaEvents(self) -> list:
        return self._listaEvents
    
    @listaEvents.setter
    def listaEvents(self, listaEvents: list) -> None:
        self._listaEvents = listaEvents
    
    
    @property
    def listaUserS(self) -> list:
        return self._listaUserS
    
    @listaUserS.setter
    def listaUserS(self, listaUserS: list) -> None:
        self._listaUserS = listaUserS
    
    
    def toList(self, evento) -> list:
        self._agenda.append(evento)
        
    def to_dict(self):
        return {"name": self.name, "listaEvents": self.listaEvents, "listaUserS": self.listaUserS}
    