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
    
    @abstractmethod #Guarda un nuevo evento
    def save_evento(self, evento: Evento):
        pass

    @abstractmethod #Actualiza un evento existente
    def actu_evento(self, id: int, evento: Evento):
        pass
    
    @abstractmethod #Elimina un evento existente
    def delete_evento(self, id: int):
        pass