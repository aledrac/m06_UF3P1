from abc import ABC, abstractmethod

from typing import List
from AUsuario import AUsuario

class IUsuarioPersistencia(ABC):
    
    @abstractmethod 
    def guarda_usuario(self, lista) -> AUsuario:
        pass
    
    @abstractmethod 
    def muestra_usuario(self,valor) -> AUsuario:
        pass

    @abstractmethod 
    def update_usuario(self,nuevoUser,valor) -> AUsuario:
        pass
    
    @abstractmethod 
    def delete_usuario(self,valor) -> AUsuario:
        pass
 