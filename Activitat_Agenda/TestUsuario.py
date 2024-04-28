import unittest
from Persistencia_mongo_Usuario import Usuario_persistencia
from Usuario import Usuario

class AtestsUsuario(unittest.TestCase):

    def test_guarda_usuario(self):
        persist = Usuario_persistencia()
        resultado = persist.guarda_usuario(Usuario("Joel","Casas","Joel@gmail.com","1234"))
        self.assertTrue(resultado)
    
    def test_update(self):
        persist = Usuario_persistencia()

        agregamos = persist.guarda_usuario(Usuario("Angel","Helbingens","angel@gmail.com","1234"))
        resultado = persist.update_usuario(Usuario("Daniel","Casas","Daniel@gmail.com","1234"),"Angel")

        self.assertEquals(resultado,0)

    def test_read(self):
        persist = Usuario_persistencia()
        
        agregamos = persist.guarda_usuario(Usuario("Lucas","Helbingens","Lucas@gmail.com","1234"))
        mostraremos = persist.muestra_usuario("Lucas")
        self.assertEquals(mostraremos,agregamos)

    def test_delete(self):
        persist = Usuario_persistencia()