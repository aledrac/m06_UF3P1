import unittest
from Usuario import Usuario
from Persistencia_mongo_Agenda import Persistencia_mongo_Agenda
from Persistencia_mongo_Usuario import Usuario_persistencia
from Agenda import Agenda
from Eventos import Evento

class TestAgenda(unittest.TestCase):
    

    def test_save_agenda(self):
        pwd = "Angel"
        user = "Angel"
        cluster = "cluster0.rvcmuq8"
        uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
        persistencia = Persistencia_mongo_Agenda(uri)
        name ="agenda1"
        nameUser = "david"
        eventos = [["28-04-2024", "4 horas", "practica m6", "estudio", "bcn", "test para mongodb"],["05-02-2024", "10 horas", "practica m7", "estudio", "barcelona", "aplicació mobile"]]
        inserted = persistencia.save_agenda(name, nameUser, eventos)
        self.assertTrue(inserted)

        
    def test_get_agenda(self):
        pwd = "Angel"
        user = "Angel"
        cluster = "cluster0.rvcmuq8"
        uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
        persistencia = Persistencia_mongo_Agenda(uri)
        agenda_get = persistencia.read_agenda()
        self.assertTrue(agenda_get)
    
    def test_get_agenda_valor(self):
        pwd = "Angel"
        user = "Angel"
        cluster = "cluster0.rvcmuq8"
        uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
        persistencia = Persistencia_mongo_Agenda(uri)
        name = "agenda1"
        agenda_valor = persistencia.read_agenda_id(name)
        self.assertTrue(agenda_valor)
        
        
    def test_update_agenda(self):
        pwd = "Angel"
        user = "Angel"
        cluster = "cluster0.rvcmuq8"
        uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
        persistencia = Persistencia_mongo_Agenda(uri)
        agenda1 = Agenda("agenda1", 
                      [["25-03-2024", "10 horas", "practica m6", "estudio", "barcelona", "test para mongodb"]], 
                      [["david", "hernandez", "david@gmail.com", "daviddavid"]])
        name = "agenda1"
        upd = persistencia.update_agenda(name, agenda1)
        self.assertTrue(upd)
        
    def test_deleted_agenda(self):
        pwd = "Angel"
        user = "Angel"
        cluster = "cluster0.rvcmuq8"
        uri = "mongodb+srv://" + \
            user + ":" + pwd + \
            "@" + cluster + ".mongodb.net/?retryWrites=true&w=majority"
        persistencia = Persistencia_mongo_Agenda(uri)
        name = "agenda1"
        deleted = persistencia.delete_agenda(name)
        self.assertTrue(deleted)
        
        
        
        

if __name__ == '_main_':
    unittest.main()