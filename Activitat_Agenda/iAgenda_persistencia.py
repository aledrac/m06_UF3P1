from abc import ABC, abstractmethod

from typing import List

class IAgendaDigital(ABC):
    @abstractmethod
    def list_events(self) -> List[dict]:
        """Da una lista de todos los eventos."""
        pass

    @abstractmethod
    def event_id_list(self, id: int) -> List[dict]:
        """Da una lista paginada de eventos según el ID."""
        pass
    
    @abstractmethod
    def save_event(self, evento: dict) -> dict:
        """Guarda un nuevo evento."""
        pass

    @abstractmethod
    def actu_event(self, id: str, evento: dict) -> dict:
        """Actualiza un evento existente."""
        pass

    @abstractmethod
    def read_event_tag(self, id: str) -> dict:
        """Lee un evento a partir de su tag."""
        pass