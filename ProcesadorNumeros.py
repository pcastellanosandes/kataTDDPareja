__autor__= 'Paula Castellanos'

class ProcesadorNumeros:
    def procesarListaNumeros (self, cadena):
        resultado = [4]
        numeros = cadena.split(',')
        resultado[0] = len(numeros)
        return resultado
