import unittest
import pymongo
from Eventos import Evento
#from PersistenciaMongo import read,create,update,delete

class TestingMetodos(unittest.TestCase):
    def test_read(self):
        ev = Evento(123, "hoy", "1 hora", "quedada en telepizza.", "TZP", "Barcelona", "hoy es jueves" )
        evento_obtenido = ev.id
        self.assertEqual(evento_obtenido,123)
    
    def connect():
        pwd = "Angel"
        user = "Angel"

    def test_read(self):
        pass

    def test_create(self):
        pass
    
    def test_update(self):
        pass
    
    def test_delete(self):
        pass

if __name__ == '__main__':
    unittest.main()