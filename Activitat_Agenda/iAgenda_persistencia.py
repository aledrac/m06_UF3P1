from abc import ABC, abstractmethod
from typing import List
from Agenda import Agenda


class IAgenda_Persistencia(ABC):
    
    @abstractmethod
    def read_agenda(self) -> List[Agenda]:
        pass
    
    @abstractmethod
    def read_agenda_id(self, id: str) -> Agenda:
        pass
    
    @abstractmethod
    def save_agenda(self, agenda: Agenda):
        pass
    
    @abstractmethod
    def update_agenda(self, id: str, agenda: Agenda):
        pass
    
    @abstractmethod
    def delete_agenda(self, id: str):
        pass