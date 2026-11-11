import math
class variable:
    idVariable:int
    coeficiente:int
    def __init__(self,idVariable,coeficiente) -> None:
        self.idVariable = idVariable
        self.coeficiente = coeficiente
class variables:
    listaVariables = []
    def variablesConCoeficientesPositivos(self):
        return [x for x in self.listaVariables if x.coeficiente>0]
class comparacion:
    def comparar(self, n1, n2):
        raise NotImplementedError()
class greaterEqual(comparacion):
    def comparar(self, n1, n2):
        return n1 >= n2
class greaterThan(comparacion):
    def comparar(self, n1, n2):
        return n1 > n2
class lessEqual(comparacion):
    def comparar(self, n1, n2):
        return n1 <= n2
class lessThan(comparacion):
    def comparar(self, n1, n2):
        return n1 < n2
class equal(comparacion):
    def comparar(self, n1, n2):
        return n1 == n2
class ecuacion:
    izquierda:variable
    derecha:variables
    simbolo:comparacion
    def variablesConCoeficientesPositivos(self):
        return self.derecha.variablesConCoeficientesPositivos()
    def ajustarVariable(self, variableEntrante)->int:
        raise NotImplementedError()
    def pivotear(self, variableEntrante):
        raise NotImplementedError()
    def reemplazarVariablePorEcuacion(self, restriccionAjusta):
        raise NotImplementedError()
def crearListaEleccion(ecu:variables)->list[int]:
    ...
def simplex(aMaximizar:ecuacion, restricciones:list[ecuacion])->list[int]:
    cantidadVariables = len(restricciones[0].derecha.listaVariables)
    cantidadRestricciones = len(restricciones)
    eleccion = crearListaEleccion(restricciones[0].derecha)
    positivas = aMaximizar.variablesConCoeficientesPositivos()
    while positivas != []:
        variableEntrante = max(positivas, key=lambda x: x.coeficiente)
        minCantidad=0
        restriccionAjusta=None
        for r in restricciones:
            if r.ajustarVariable(variableEntrante) < minCantidad:
                minCantidad = r.ajustarVariable(variableEntrante)
                restriccionAjusta = r
        if restriccionAjusta == None: raise Exception("ubounded linear system")
        restriccionAjusta.pivotear(variableEntrante)
        aMaximizar.reemplazarVariablePorEcuacion(restriccionAjusta)
        for r in restricciones:
            r.reemplazarVariablePorEcuacion(restriccionAjusta)
    return eleccion
    # probelma con forma slack
    # seleccionar una solucion básica
    # mientras exista una variable con coeficiente positivo en la ecu a maximizar
    #   selecionar v_{e} entre las que tengan coeficiente positivo
    #   determinar la variable basica de salida v_{s} que ajusta a v_{e}
    #   Si no se ajusta retornar infinito
    #   pivotear v_{e} y v_{s}
    #   reemplazar v_{e} por la ecuacion en todas las restricciones y la ecu a maximizar
    # retornar las variables de decision y el valor de la funcion objetivo
    return []