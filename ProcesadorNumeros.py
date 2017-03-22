__autor__= 'Paula Castellanos'

class ProcesadorNumeros:
    def procesarListaNumeros (self, cadena):
        resultado = [0]*4
        if cadena == "":
            resultado[0] = 0
        else:
            numeros = cadena.split(',')
            resultado[0] = len(numeros)
        resultado[1] = 0
        return resultado
