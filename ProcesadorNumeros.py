__autor__= 'Paula Castellanos'

class ProcesadorNumeros:
    def procesarListaNumeros (self, cadena):
        resultado = [4]
        numeros = cadena.split(',')
        if(cadena == ""):
            resultado[0] = 0
        elif ',' in cadena:
            resultado[0] = 2
        else:
            resultado[0] = 1
        return resultado

