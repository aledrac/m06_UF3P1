import unittest
from unittest.mock import MagicMock
from iUsuario_persistencia import iUsuario_persistencia

class TestUsuarioPersistencia(unittest.TestCase):

    def setUp(self):
        self.persistencia = iUsuario_persistencia("1", "2", "3", "4")
        self.persistencia.conectar_usuario = MagicMock()
        mock_db = MagicMock()
        mock_collection = MagicMock()
        self.persistencia.conectar_usuario.return_value = mock_db
        mock_db.miBaseDeDatos = MagicMock()
        mock_db.miBaseDeDatos.Usuarios = mock_collection
        mock_db.miBaseDeDatos.Usuarios.insert_one.return_value.inserted_count = 1
        mock_db.miBaseDeDatos.Usuarios.insert_many.return_value.inserted_count = 2


    def test_guarda_usuario(self):
        usuarios = [
            {"name": "Joel", "apellido": "Casas", "mail": "joel@gmail.com", "pwd": "1234"},
            {"name": "Dani", "apellido": "Casas", "mail": "dani@gmail.com", "pwd": "abcd"}
        ]
        resultado = self.persistencia.guarda_usuario(usuarios)
        self.assertEqual(resultado, 2)
    
    def test_muestra_usuario(self):
        user1 = iUsuario_persistencia("Angel","","","")
        user2 = iUsuario_persistencia("","","","")
        usuariosAgregados = []

    def test_delete_usuario(self):
        usuarios = [
            {"name": "Angel", "apellido": "Helbingens", "mail": "angelo@gmail.com", "pwd": "6666"}
        ]
        resultado = self.persistencia.guarda_usuario(usuarios)
        self.assertIsNotNone(resultado)
        #Comprobar que existe
        usuarioExiste = self.persistencia.muestra_usuario("angel")
        #Comprobar que se a eliminado
        
    
    