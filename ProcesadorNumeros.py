__autor__= 'Paula Castellanos'

class ProcesadorNumeros:
    def procesarListaNumeros (self, cadena):
        resultado = [0]*4
        resultado[0] = self.calcularCantidadNumeros(cadena)
        resultado[1] = self.calcularMinimo(cadena)
        return resultado

    def calcularCantidadNumeros(self, cadena):
        resultado = 0
        if cadena != "":
            numeros = cadena.split(',')
            resultado = len(numeros)
        return resultado

    def calcularMinimo(self, cadena):
        numeros = cadena.split(',')
        numeros.reverse()
        return numeros[0]