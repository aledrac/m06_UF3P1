import unittest
from unittest.mock import MagicMock
from Persistencia_mongodb import Persistencia_agenda_mongodb
from Eventos import Evento

class TestPersistenciaAgendaMongoDB(unittest.TestCase):

    





    #region Old code
    def setUp(self):
        self.persistencia = Persistencia_agenda_mongodb()
        self.persistencia.conection = MagicMock()

    def test_read_evento_tag(self):
        self.persistencia.conection.evento.find.return_value = [
            {'_id': '1', 'fecha': '2024-04-20', 'duracion': 2, 'titulo': 'Evento Test', 'tag': 'test', 'ubicacion': 'Oficina', 'descripcion': 'Descripción del evento Test'}
        ]
        eventos = self.persistencia.read_evento_tag('test')
        self.assertEqual(len(eventos), 1)
        self.assertIsInstance(eventos[0], Evento)

    def test_save_evento(self):
        evento = Evento('1', '2024-04-20', 2, 'Evento Test', 'test', 'Oficina', 'Descripción del evento Test')
        evento.to_dict = MagicMock(return_value={'_id': '1', 'fecha': '2024-04-20', 'duracion': 2, 'titulo': 'Evento Test', 'tag': 'test', 'ubicacion': 'Oficina', 'descripcion': 'Descripción del evento Test'})
        self.persistencia.save_evento(evento)
        self.persistencia.conection.evento.insert_one.assert_called_with(evento.to_dict())

    def test_delete_evento(self):
        self.persistencia.delete_evento('1')
        self.persistencia.conection.evento.delete_one.assert_called_with({"_id": '1'})
    
    #endregion

if __name__ == '__main__':
    unittest.main()
