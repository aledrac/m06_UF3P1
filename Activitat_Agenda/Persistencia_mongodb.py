from typing import List

from bson import ObjectId
from iAgenda_persistencia import IAgendaDigital
from Agenda import Agenda
from Eventos import Evento 
import pymongo

class Persistencia_agenda_mongodb(IAgendaDigital):
    
    pwd = "Angel"
    user = "Angel"
    cluster = "cluster0.rvcmuq8"
    uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
    conection = pymongo.MongoClient(uri)
  
  
    #Da una lista de eventos a partir de su tag
    def read_evento_tag(self, tag: str) -> List[Evento]:
        lista_tag = self.conection.evento.find({ "tag" : tag})
        eventos = []
        for e in lista_tag:
            eventos.append(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7]) 
        return eventos
    
    #Da una lista de todos los eventos
    def lista_eventos(self) -> List[Evento]:
        lista_evento  = self.conection.evento.find()
        eventos = []
        for e in lista_evento:
            eventos.append(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7]) 
        return eventos

    #Da una evento por id
    def evento_id(self, id: int) -> Evento:
        eventoId = self.conection.evento.find_one({"_id": ObjectId(id)})
        if eventoId:
            e = Evento(
                id=eventoId["_id"],
                fecha = eventoId["fecha"],
                duracion=eventoId["duracion"],
                titulo=eventoId["titulo"],
                tag=eventoId["tag"],
                ubicacion=eventoId["ubicacion"],
                desc=eventoId["descripcion"]
            )
        return e
    
    #Guarda un nuevo evento
    def save_evento(self, evento: Evento) -> Evento:
        self.conection.evento.insert_one(evento.to_dict())
        #query = "db.agenda.insert({ _id: '', duracio: '', titulo: '', tag: '', ubicacion: '', desc: ''})"
        
    #Actualiza un evento existente
    def actu_evento(self, id: int, evento: Evento) -> Evento:
        self.conection.evento.update_one({"_id": ObjectId(id)},
                                        {"$set": evento.to_dict()})
    
    #Elimina un evento existente
    def delete_evento(self, id: int) -> Evento:
        self.conection.evento.delete_one({"_id": ObjectId(id)})
        #query = "db.agenda.remove({ _id: '1'})"