from unittest import TestCase
from ProcesadorNumeros import ProcesadorNumeros

class TestProcesadorNumeros(TestCase):

    def test_ListaVacia(self):
        self.assertEqual(ProcesadorNumeros().procesarListaNumero(""), 0, "Validar cadena vacia")

    def test_ListaUnNumero(self):
        self.assertEqual(ProcesadorNumeros().procesarListaNumero("12"), 1, "Validar cadena un numero")