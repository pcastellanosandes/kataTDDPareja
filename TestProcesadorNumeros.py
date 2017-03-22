from unittest import TestCase
from ProcesadorNumeros import ProcesadorNumeros

class TestProcesadorNumeros(TestCase):

    def test_ListaVacia(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("")
        self.assertEqual(resultado[0], 0, "Validar cadena vacia")

    def test_ListaUnNumero(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("12")
        self.assertEqual(resultado[0], 1, "Validar cadena un numero")

    def test_ListaDosNumeros(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("12,2")
        self.assertEqual(resultado[0], 2, "Validar cadena con dos numeros")

    def test_ListaNNumeros(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("12,2,44")
        self.assertEqual(resultado[0], 3, "Validar cadena con n  numeros")