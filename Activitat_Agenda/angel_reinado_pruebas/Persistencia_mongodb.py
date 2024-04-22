from typing import List
from iEvento_persistencia import IEventoDigital
from Agenda import Agenda
from Eventos import Evento
import pymongo

class Persistencia_agenda_mongodb(IEventoDigital):

    uri = ""
    conexionPortable = pymongo.MongoClient(uri)
    def __init__(self,user,pwd,cluster):
        self.uri = "mongodb+srv://"+user+":"+pwd+"@"+cluster+".mongodb.net/?retryWrites=true&w=majority"
  
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


#Clase creada solamente para ingresar informacion
class app():
    def main():
        conexion = Persistencia_agenda_mongodb("Angel","Angel","cluster0.rvcmuq8")
        


    if __name__ == '__main__':
        main()