from typing import List
from iAgenda_persistencia import IAgenda_persistencia
from agenda import Agenda
from eventos import Evento 

class Persistencia_agenda_mongodb(IAgenda_persistencia):
  
    #Da una lista de eventos a partir de su tag
    def read_evento_tag(self, tag: str) -> List[Evento]:
        query = "db.agenda.find({ tag: '' })"
    
    #Da una lista de todos los eventos
    def lista_eventos(self) -> List[Evento]:
        query = "db.agenda.find()"

    #Da una evento por id
    def evento_id(self, id: int) -> Evento:
       query = "db.agenda.find({ _id: '' })"
    
    #Guarda un nuevo evento
    def save_evento(self, evento: Evento) -> Evento:
        query = "db.agenda.insert({ _id: '', duracio: '', titulo: '', tag: '', ubicacion: '', desc: ''})"
    #Actualiza un evento existente
    def actu_evento(self, id: int, evento: Evento) -> Evento:
        query = ""
    
    #Elimina un evento existente
    def delete_evento(self, id: int) -> Evento:
        query = "db.agenda.remove({ _id: '1'})"