import datetime
from iEvento_persistencia import IEventoDigital

class Evento(IEventoDigital):
    def __init__(self, id: int,  fecha: str, duracion: str, titulo: str, tag: str, ubicacion: str, descripcion="" ) -> None:
        self._id = id
        self._fecha = fecha
        self._duracion = duracion
        self._titulo = titulo
        self._tag = tag
        self._ubicacion = ubicacion
        self._descripcion = descripcion
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id:int) -> None:
        self._id = id
        
    @property
    def fecha(self) -> str:
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha:str) -> None:
        self._fecha = fecha
    
    @property
    def duracion(self) -> str:
        return self._duracion
    
    @duracion.setter
    def duracion(self, duracion:str) -> None:
        self._duracion = duracion
        
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo:str) -> None:
        self._titulo = titulo
        
    @property
    def tag(self) -> str:
        return self._tag
    
    @tag.setter
    def tag(self, tag:str) -> None:
        self._tag = tag
    
    @property   
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, ubicacion:str) -> None:
        self._ubicacion = ubicacion
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion:str) -> None:
        self._descripcion = descripcion
        
    
    def to_dict(self):
        return {"_id": self._id, "duracion": self.duracion, "titulo": self.titulo, "tag": self.tag, "ubicacion": self.ubicacion, "desc": self.desc}
        
    