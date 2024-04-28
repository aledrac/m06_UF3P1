import unittest
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
        esdeveniment = Agenda("agenda1", 
                      [["28-04-2024", "4 horas", "practica m6", "estudio", "bcn", "test para mongodb"]], 
                      [["david", "hernandez", "david@gmail.com", "daviddavid"]])
        inserted = persistencia.save_agenda(esdeveniment)
        self.assertTrue(inserted)
    
if _name_ == '_main_':
    unittest.main()