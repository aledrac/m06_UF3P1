
class Agenda:
    def __init__(self, agenda: list) -> None:
        self._agenda = agenda
        
    @property
    def agenda(self) -> list:
        return self._agenda
    
    @agenda.setter
    def agenda(self, agenda: list) -> None:
        self._agenda = agenda
        
    def toList(self, evento) -> list:
        self._agenda.append(evento)
    