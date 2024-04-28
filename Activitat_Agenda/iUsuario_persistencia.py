from abc import ABC, abstractmethod

from typing import List
from Usuario import Usuario

class IUsuarioPersistencia(ABC):
    
    @abstractmethod 
    def read_user(self, valor) -> List[Usuario]:
        pass

    @abstractmethod 
    def read_user_valor(self, valor) -> Usuario:
        pass
    
    @abstractmethod 
    def save_user(self, user: Usuario):
        pass

    @abstractmethod 
    def update_user(self, name, user: Usuario):
        pass
    
    @abstractmethod 
    def delete_user(self, valor):
        pass
 