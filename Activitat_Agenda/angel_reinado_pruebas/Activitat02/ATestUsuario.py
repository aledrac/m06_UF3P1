import unittest
from APersistencia_Usuario import Usuario_persistencia
from AUsuario import AUsuario

class AtestsUsuario(unittest.TestCase):

    def test_guarda_usuario(self):
        persistencia = Usuario_persistencia()
        us1 = AUsuario("Joel","Casas","Joel@gmail.com","1234")
        resultado = persistencia.guarda_usuario(us1)
        self.assertIsNotNone(resultado)