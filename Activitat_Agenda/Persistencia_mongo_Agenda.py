from typing import List
import pymongo 
from Eventos import Evento
from Usuario import Usuario
from Agenda import Agenda
from iAgenda_persistencia import IAgenda_Persistencia

class Persistencia_mongo_Agenda(IAgenda_Persistencia):
   
    def __init__(self, uri) :
        self.conection = pymongo.MongoClient(uri)
        self.db = self.conection.agendadb
        self.coleccio = self.db.agenda 
    
    
    def read_agenda(self) -> List[Agenda]:
        return list(self.coleccio.find())
    
    def read_agenda_id(self, name: str):
        return self.coleccio.find({"name": name})
    
    def save_agenda(self, agenda:Agenda):
        #user_cursor = self.coleccio2.find({"name": nameUser})
        #user = list(user_cursor)
        #if not user: return "no s'ha trobat l'usuari"
        #agenda = Agenda(name, user, evento)
        agenda_dict = agenda.to_dict()
        ins = self.coleccio.insert_one(agenda_dict)
        return ins.acknowledged
    
    def update_agenda(self, name: str, agenda: Agenda):
        filtro = { "name": name }  
        actualizacion = { "$set": agenda.to_dict() }  
        mod = self.coleccio.update_one(filtro, actualizacion)
        return mod.modified_count
    
    def delete_agenda(self, name: str):
        deleted = self.coleccio.delete_one({"name": name})
        return deleted.deleted_count