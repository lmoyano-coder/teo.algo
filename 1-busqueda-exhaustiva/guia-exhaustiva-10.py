# 10. En una variante del problema de la mochila, tenemos “n” elementos que podemos
# incluir dentro de un contenedor que acepta un total de “K” kilos. Cada elemento tiene un
# peso, un valor y un subconjunto de otros elementos con el que es incompatible
# seleccionarlo. Debemos seleccionar la combinación de elementos que sume el mayor
# valor posible sin incumplir las restricciones. En caso de existir diferentes soluciones
# máximas se prefiere a aquella que requiere un menor peso. Resolver por branch and
# bound.
import random
class elemento:
    peso:int
    valor:int
    e_incompatible:list
    def __init__(self, peso, valor, e_incompatible):
        self.peso = peso
        self.valor = valor
        self.e_incompatible = e_incompatible
    def nuevo_incompatible(self, inco):
        if inco not in self.e_incompatible:
            self.e_incompatible.append(inco)
    def incompatible(self, otro_elemento):
        return otro_elemento in self.e_incompatible 

class restricciones:
    peso_maximo:int 
    elementos:list
    def __init__(self,peso_maximo, elementos):
        self.elementos = elementos
        self.peso_maximo = peso_maximo

def posibles_elementos(estado_actual, problema:restricciones):
    if estado_actual == [] or estado_actual == None:
            return problema.elementos
    disponibles = problema.elementos.copy()
    for d in disponibles:
        for e_elegido in estado_actual:
            if e_elegido.incompatible(d) or e_elegido == d:
                disponibles.remove(d)
    return disponibles
def estados_posibles_proximos(estado_actual, problema):
    estados_posibles = []
    elementos_posibles = posibles_elementos(estado_actual, problema)
    if estado_actual == None:
        estado_actual = []
    print("estados_posibles_proximos:")
    for e in elementos_posibles:
        print("(",e.peso,",",e.valor,")")
        copia = estado_actual.copy()
        print("copia: ",copia.append(e))

        estados_posibles.append(copia.append(e))

    return estados_posibles
def mejor_por_unidad(elementos):
    return sorted(elementos, key=lambda e: e.valor/e.peso, reverse=True)[0]
def peso_elementos(estado_actual):
    if estado_actual == [] or estado_actual == None:
            return 0
    peso_total = 0
    for i in estado_actual:
        peso_total += i.peso
    return peso_total
def costo(estado_actual):
    if estado_actual == [] or estado_actual == None:
        return 0
    valor_total = 0
    print(estado_actual.peso, " ", estado_actual.valor)
    for e in estado_actual:
        valor_total += e.valor
    return valor_total
def costo_estimado(estado_actual, problema):
    elementos = problema.elementos
    peso_maximo = problema.peso_maximo
    valor_actual = costo(estado_actual)
    mejor_elemento = mejor_por_unidad(posibles_elementos(estado_actual, problema))
    valor_unidad = mejor_elemento.valor/mejor_elemento.peso
    peso_disponible = peso_maximo - peso_elementos(estado_actual)
    return valor_actual + peso_disponible * valor_unidad
def mostrar_elementos(elementos):
    if elementos == None:
        print("[]")
        return
    for i in elementos:
        print("(",i.peso,",",i.valor,")", end=" ")
    print("")
def mochila_branch_bound_imcompatibles(estado_actual, estado_mejor, problema):
    peso_maximo:int = problema.peso_maximo
    # mostrar_elementos(estado_actual)
    if estado_actual == None:
        print("estado_actual None")
    if estado_actual == None:
        print("estado_mejor None")
    if estado_mejor == [] or estado_mejor == None:
        estado_mejor = estado_actual
    if peso_elementos(estado_actual) > peso_maximo:
        return estado_mejor
    if costo(estado_actual) > costo(estado_mejor):
        return estado_actual.copy()
    if costo_estimado(estado_actual,problema) < costo_estimado(estado_mejor,problema):
        return estado_mejor
    cola_hijos:list = estados_posibles_proximos(estado_actual, problema)
    cola_hijos.sort(key=lambda h: costo_estimado(h,problema), reverse=True)
    mostrar_elementos(cola_hijos)
    for i in cola_hijos:
        estado_mejor = mochila_branch_bound_imcompatibles(i, estado_mejor, problema)
    return estado_mejor
def generar_elemento(pes_min, pes_max, val_min, val_max):
    peso = random.randint(pes_min,pes_max) + 0.1 + random.random()
    valor = random.randint(val_min, val_max) + 0.1 + random.random()
    return elemento(peso, valor, [])
def generar_problema(peso_max, cant_elementos):
    elementos_lista:list = []
    for i in range(cant_elementos):
        elementos_lista.append(generar_elemento(0,peso_max//2,0,10))
    problema = restricciones(peso_max, elementos_lista)
    print("elementos: ", end="")
    mostrar_elementos(problema.elementos)
    solucion = mochila_branch_bound_imcompatibles([],[],problema)
    print("solucion: ", end="")
    mostrar_elementos(solucion)
generar_problema(10, 3)