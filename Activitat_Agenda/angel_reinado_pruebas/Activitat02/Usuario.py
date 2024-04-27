from abc import ABC, abstractmethod
from typing import List
from Usuario import Usuario

class usuario(ABC):
    
    #region ///////Metodos principales
    @abstractmethod
    def guarda_usuario( self,lista ) -> bool:
        pass
    
    @abstractmethod
    def delete_usuario(self) -> bool:
        pass

    @abstractmethod
    def update_usuario(self) -> bool:
        pass

    @abstractmethod
    def muestra_usuario(self) -> bool:
        pass
    #endregion

    
    #region ///////Metodos secundarios
    @abstractmethod
    def comprueba_existencia(self):
        pass
    #endregion
