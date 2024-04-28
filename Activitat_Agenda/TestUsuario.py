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
        u1 = "Joel"
        lectura = persist.muestra_usuario(u1)
        self.assertTrue(lectura)

    def test_delete(self):
        persist = Usuario_persistencia()
        deleted = persist.delete_usuario("joel")
        self.assertFalse(deleted)