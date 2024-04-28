import unittest
from APersistencia_Usuario import Usuario_persistencia
from AUsuario import AUsuario

class AtestsUsuario(unittest.TestCase):

    def test_guarda_usuario(self):
        persist = Usuario_persistencia()
        resultado = persist.guarda_usuario(AUsuario("Joel","Casas","Joel@gmail.com","1234"))
        self.assertTrue(resultado)
    
    def test_update(self):
        persist = Usuario_persistencia()

        agregamos = persist.guarda_usuario(AUsuario("Angel","Helbingens","angel@gmail.com","1234"))
        resultado = persist.update_usuario(AUsuario("Daniel","Casas","Daniel@gmail.com","1234"),"Angel")

        self.assertEquals(resultado,0)

    def test_read(self):
        persist = Usuario_persistencia()
        
        agregamos = persist.guarda_usuario(AUsuario("Lucas","Helbingens","Lucas@gmail.com","1234"))
        mostraremos = persist.muestra_usuario("Lucas")

    def test_delete(self):
        persist = Usuario_persistencia()