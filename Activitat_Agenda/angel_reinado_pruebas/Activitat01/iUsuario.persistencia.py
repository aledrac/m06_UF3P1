from abc import ABC, abstractmethod

from typing import List
from Usuario import Usuario

class IUsuarioPersistencia(ABC):
    
    @abstractmethod #Da una lista de eventos a partir de su tag
    def read_user(self, valor) -> Usuario:
        pass
    
    @abstractmethod #Da una lista de todos los eventos
    def lista_users(self) -> List[Usuario]:
        pass

    @abstractmethod #Da una evento por id
    def user_id(self, id: str) -> Usuario:
        pass
    
    @abstractmethod #Guarda un nuevo evento
    def save_user(self, user: Usuario) -> Usuario:
        pass

    @abstractmethod #Actualiza un evento existente
    def actu_user(self, id: str, user: Usuario) -> Usuario:
        pass
    
    @abstractmethod #Elimina un evento existente
    def delete_user(self, id: str) -> Usuario:
        pass