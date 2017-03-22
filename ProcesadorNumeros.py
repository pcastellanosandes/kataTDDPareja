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
        numeros = self.convertirAInt(cadena)
        numeros.sort()
        return numeros[0]

    def convertirAInt(self, cadena):
        if cadena != "":
            numeros = cadena.split(',')
            return [int(numeric_string) for numeric_string in numeros]
        else:
            return [0]