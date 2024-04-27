from abc import ABC, abstractmethod
from typing import List
from Usuario import Usuario

class IUsuarioPersistencia(ABC):
    
    #region ///////Metodos principales
    @abstractmethod
    def guarda_usuario(self) -> bool:
        pass
    
    @abstractmethod
    def delete_usuario(self):
        pass

    @abstractmethod
    def update_usuario(self):
        pass

    @abstractmethod
    def muestra_usuario(self):
        pass
    #endregion

    
    #region ///////Metodos secundarios
    @abstractmethod
    def comprueba_existencia(self):
        pass
    #endregion
