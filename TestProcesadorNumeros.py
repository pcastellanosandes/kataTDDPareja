from unittest import TestCase
from ProcesadorNumeros import ProcesadorNumeros

class TestProcesadorNumeros(TestCase):

    def test_ListaVacia(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("")
        self.assertEqual(resultado[0], 0, "Validar cadena vacia")
        self.assertEqual(resultado[1], 0, "Obtener minimo de cadena vacia")

    def test_ListaUnNumero(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("12")
        self.assertEqual(resultado[0], 1, "Validar cadena un numero")
        self.assertEqual(resultado[1], 12, "Obtener minimo cadena con un numero")

    def test_ListaDosNumeros(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("12,2")
        self.assertEqual(resultado[0], 2, "Validar cadena con dos numeros")
        self.assertEqual(resultado[1], 2, "Validar minimo de cadena con dos numeros")

    def test_ListaNNumeros(self):
        resultado = ProcesadorNumeros().procesarListaNumeros("12,2,44")
        self.assertEqual(resultado[0], 3, "Validar cadena con n  numeros")

