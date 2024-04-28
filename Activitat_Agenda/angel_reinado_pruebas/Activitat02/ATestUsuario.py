import unittest
from unittest.mock import MagicMock
from APersistencia_Usuario import Usuario_persistencia

class AtestsUsuario(unittest.TestCase):

    def setUp(self):
        pass


    def test_guarda_usuario(self):
        us1 = Usuario_persistencia("Joel","Casas","Joel@gmail.com","1234")
        resultado = Usuario_persistencia.guarda_usuario(us1)
        self.assertIsNotNone(resultado)