import unittest
from Agenda import Agenda
from Eventos import Evento
from Persistencia_mongo_Agenda import Persistencia_mongo_Agenda

class TestPersistenciaAgenda(unittest.TestCase):
    
    def setUp(self):
        # Configura la persistencia de agenda
        self.persistencia_agenda = Persistencia_mongo_Agenda()

        # Crea datos de prueba
        self.agenda_prueba = Agenda(name="Mi Agenda", listaEvents=[], listaUserS=[])

    def test_guardar_leer_agenda(self):
        # Guardar agenda
        self.assertTrue(self.persistencia_agenda.save_agenda(self.agenda_prueba))
        
        # Leer agenda
        agendas = self.persistencia_agenda.read_agenda()
        self.assertIsNotNone(agendas)
        self.assertTrue(len(agendas) > 0)
        
    def test_actualizar_eliminar_agenda(self):
        # Guardar agenda
        self.assertTrue(self.persistencia_agenda.save_agenda(self.agenda_prueba))
        
        # Actualizar agenda
        self.assertTrue(self.persistencia_agenda.update_agenda(name="Mi Agenda", agenda=self.agenda_prueba))
        
        # Eliminar agenda
        self.assertTrue(self.persistencia_agenda.delete_agenda(name="Mi Agenda"))
        
if __name__ == '__main__':
    unittest.main()