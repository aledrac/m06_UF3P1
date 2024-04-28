from abc import ABC, abstractmethod

from typing import List
from Eventos import Evento 

class IEventoDigital(ABC):
    
    @abstractmethod #Da una lista de eventos a partir de su tag
    def read_evento_tag(self, tag: str) -> List[Evento]:
        pass
    
    @abstractmethod #Da una lista de todos los eventos
    def lista_eventos(self) -> List[Evento]:
        pass

    @abstractmethod #Da una evento por id
    def evento_id(self, id: int) -> Evento:
        pass
    
