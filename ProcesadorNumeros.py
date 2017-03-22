__autor__= 'Paula Castellanos'

class ProcesadorNumeros:
    def procesarListaNumeros (self, cadena):
        resultado = [4]
        numeros = cadena.split(',')
        if(cadena == ""):
            resultado[0] = 0
        else:
            resultado[0] = 1
        return resultado

