from typing import List
from iAgenda_persistencia import IAgenda_persistencia
from Agenda import Agenda
from Eventos import Evento 
import pymongo

class Persistencia_agenda_mongodb(IAgenda_persistencia):
    
    pwd = "wv2B3otgf6QKgptC"
    user = "2023davidhernandez"
    cluster = "cluster0.efsedoq"
    uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
    conection = pymongo.MongoClient(uri)
  
    #Da una lista de eventos a partir de su tag
    def read_evento_tag(self, tag: str) -> List[Evento]:
        self.conection.evento.find_one(tag)
        #query = "db.agenda.find({ tag: '' })"
    
    #Da una lista de todos los eventos
    def lista_eventos(self) -> List[Evento]:
        self.conection.evento.find()
        #query = "db.agenda.find()"

    #Da una evento por id
    def evento_id(self, id: int) -> Evento:
        self.conection.evento.find_one({"_id": id})
        #query = "db.agenda.find({ _id: '' })"
    
    #Guarda un nuevo evento
    def save_evento(self, evento: Evento) -> Evento:
        self.conection.evento.insert_one(evento)
        #query = "db.agenda.insert({ _id: '', duracio: '', titulo: '', tag: '', ubicacion: '', desc: ''})"
        
    #Actualiza un evento existente
    def actu_evento(self, id: int, evento: Evento) -> Evento:
        self.conection.evento.update_one()
        #query = ""
    
    #Elimina un evento existente
    def delete_evento(self, id: int) -> Evento:
        self.conection.evento.delete_one(id)
        #query = "db.agenda.remove({ _id: '1'})"