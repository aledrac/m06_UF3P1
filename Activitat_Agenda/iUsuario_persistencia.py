from abc import ABC, abstractmethod

from typing import List
from Usuario import Usuario

class IUsuarioPersistencia(ABC):
    
    @abstractmethod #Da una lista de eventos a partir de su tag
    def read_user(self, valor) -> List[Usuario]:
        pass

    @abstractmethod #Da una evento por id
    def read_user_valor(self, valor) -> Usuario:
        pass
 