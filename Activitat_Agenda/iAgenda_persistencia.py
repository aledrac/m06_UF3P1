from abc import ABC, abstractmethod
from typing import List
from Eventos import Evento
from Agenda import Agenda


class IAgenda_Persistencia(ABC):
    
    @abstractmethod
    def read_agenda(self) -> List[Agenda]:
        pass
    
    @abstractmethod
    def read_agenda_id(self, id: str):
        pass
    
    @abstractmethod
    def save_agenda(self, name:str, nameUser:str, evento:List[Evento]):
        pass
    
    @abstractmethod
    def update_agenda(self, id: str, agenda: Agenda):
        pass
    
    @abstractmethod
    def delete_agenda(self, id: str):
        pass