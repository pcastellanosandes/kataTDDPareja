from unittest import TestCase
from ProcesadorNumeros import ProcesadorNumeros

class TestProcesadorNumeros(TestCase):

    def test_ListaVacia(self):
        self.assertEqual(ProcesadorNumeros().procesarVacio(""), 0, "Validar cadena vacia")
