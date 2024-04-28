from abc import ABC, abstractmethod

from typing import List
from Eventos import Evento 

class IEventoDigital(ABC):
    
    @abstractmethod 
    def read_evento_tag(self, tag: str) -> List[Evento]:
        pass
    
    @abstractmethod 
    def lista_eventos(self) -> List[Evento]:
        pass

    @abstractmethod 
    def evento_id(self, id: int) -> Evento:
        pass
    
    @abstractmethod 
    def save_evento(self, evento: Evento):
        pass

    @abstractmethod 
    def actu_evento(self, id: int, evento: Evento):
        pass
    
    @abstractmethod 
    def delete_evento(self, id: int):
        pass
    
