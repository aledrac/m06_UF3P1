from typing import List
import pymongo 
from Agenda import Agenda
from iAgenda_persistencia import IAgenda_Persistencia

class Persistencia_mongo_Agenda(IAgenda_Persistencia):
    pwd = "Angel"
    user = "Angel"
    cluster = "cluster0.rvcmuq8"
    uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
    def __init__(self, uri) :
        self.conection = pymongo.MongoClient(uri)
        self.db = self.conection.agendadb
        self.coleccio = self.db.agenda 
    
    
    def read_agenda(self) -> List[Agenda]:
        return list(self.coleccio.find())
    
    def read_agenda_id(self, name: str) -> Agenda:
        return self.coleccio.find_one(name)
    
    def save_agenda(self, agenda: Agenda):
        agenda_dict = agenda.to_dict()
        ins = self.coleccio.insert_one(agenda_dict)
        return ins.asknowledged()
    
    def update_agenda(self, name: str, agenda: Agenda):
        filtro = { "name": name }  
        actualizacion = { "$set": agenda.to_dict() }  
        mod = self.coleccio.update_many(filtro, actualizacion)
        return mod.modified_count()
    
    def delete_agenda(self, name: str):
        deleted = self.coleccio.delete_one(name)
        return deleted.deleted_count()