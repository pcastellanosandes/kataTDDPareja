__autor__= 'Paula Castellanos'

class ProcesadorNumeros:
    def procesarListaNumeros (self, cadena):
        resultado = [0]*4
        numeros = self.convertirAInt(cadena)
        resultado[0] = self.calcularCantidadNumeros(numeros)
        resultado[1] = self.calcularMinimo(numeros)
        return resultado

    def calcularCantidadNumeros(self, numeros):
        resultado = len(numeros)
        return resultado

    def calcularMinimo(self, numeros):
        numeros.sort()
        if len(numeros) > 0:
            return numeros[0]
        else:
            return 0

    def convertirAInt(self, cadena):
        nums = []
        if cadena != "":
            numeros = cadena.split(',')
            for num in numeros:
                nums.append(int(num))

        return  nums
