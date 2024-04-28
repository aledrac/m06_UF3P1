import unittest
from Agenda import Agenda
from Eventos import Evento

class TestAgenda(unittest.TestCase):
    
    def setUp(self):
        # Crear algunos eventos de ejemplo
        self.evento1 = Evento(id=1, fecha="2024-05-01", duracion="2 horas", titulo="Reunión", tag="trabajo", ubicacion="Oficina")
        self.evento2 = Evento(id=2, fecha="2024-05-02", duracion="1 hora", titulo="Entrevista", tag="trabajo", ubicacion="Zoom")
        self.evento3 = Evento(id=3, fecha="2024-05-03", duracion="3 horas", titulo="Fiesta", tag="personal", ubicacion="Casa")
        
        # Crear una lista de eventos
        self.lista_eventos = [self.evento1, self.evento2, self.evento3]
        
        # Crear una instancia de Agenda con los eventos de ejemplo
        self.agenda = Agenda(name="Mi Agenda", listaEvents=self.lista_eventos, listaUserS=[])
    
    def test_name(self):
        self.assertEqual(self.agenda.name, "Mi Agenda")
        
    def test_listaEvents(self):
        self.assertEqual(len(self.agenda.listaEvents), 3)  # Comprueba si hay 3 eventos en la lista
    
    def test_agregar_evento(self):
        # Crea un nuevo evento y lo agrega a la agenda
        nuevo_evento = Evento(id=4, fecha="2024-05-04", duracion="1 hora", titulo="Conferencia", tag="trabajo", ubicacion="Sala de conferencias")
        self.agenda.toList(nuevo_evento)
        self.assertEqual(len(self.agenda.listaEvents), 4)  # Comprueba si se ha agregado el nuevo evento
        
    # Agrega más métodos de prueba según sea necesario
    
if _name_ == '_main_':
    unittest.main()