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
    conection = pymongo.MongoClient(uri)
    
    def read_agenda(self) -> List[Agenda]:
        return list(self.conection.agenda.find())
    
    def read_agenda_id(self, name: str) -> Agenda:
        return self.conection.find(name)
    
    def save_agenda(self, agenda: Agenda):
        agenda_dict = agenda.to_dict()
        ins = self.conection.insert_one(agenda_dict)
        return ins.asknowledged()
    
    def update_agenda(self, name: str, agenda: Agenda):
        filtro = { "name": name }  
        actualizacion = { "$set": agenda.to_dict() }  
        mod = self.conection.update_many(filtro, actualizacion)
        return mod.modified_count()
    
    def delete_agenda(self, name: str):
        deleted = self.conection.delete_one(name)
        return deleted.deleted_count()