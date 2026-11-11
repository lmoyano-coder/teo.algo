# 2. Definimos el problema de la partición uniforme del grafo como: Dado un grafo completo
# G=(V,E), con cantidad de nodos par, con pesos en sus ejes enteros positivos y el cero.
# Queremos dividir sus nodos en dos conjuntos A, B de igual cantidad de elementos
# buscando minimizar la suma costos de los ejes e=(u,v) con u ∈ A y v ∈ B. Proponer
# resolver este problema utilizando Simulated Annealing.

# Para simulated annealing necesito: 
# funcion vecinos, temperatura, constante enfriamiento, funcion costo y cantidad de iteraciones.
# funcion costo: \sum_{i=0}^{n}costo(e=(u,v)), siendo n la cantidad de ejes que cumplen 
# e=(u,v) con u ∈ A y v ∈ B. cantidad de iteraciones nos la dan.
# la solución será un vector de largo V, que represente los nodos, con 0 para A y 1 para B.
# con la posición i correspondiente al i-ésimo nodo.
# vecinos: si s_{a} la solucion actual, sus vecinos serán de la forma s_{v} si:
# s_{v}[i] = 1 - s_{a}[i], s_{v}[j] = 1 - s_{a}[j], j != i
# es decir, vecinos a dos cambios de distancia.

# Sea costo la funcion que sea la suma de las aristas de la frontera entre A y B
# sea vecinos la funcion que de todos lo vecinos a 2 cambios de distancia de una sol. particular.
# Sea T=T_{0}, c la constante de enfriamiento, Max el maximo de iteraciones, it=0
# s_{m} la mejor solucion, s_{a} la actual. establecerlos en la solucion inicial (lista de 0s)
# Mientras it<Max:
#   s_{v} = elegir aleatoriamente un vecino de vecinos(s_{a})
#   s_{a} = proximoEstado(s_{a},s_{v},T)
#   s_{m} = el maximo entre s_{a} y s_{m}
#   T = T * c
#   it+=1
# devolver s_{m} 
# def proximoEstado(s_a, s_v, T):
#   Si costo(s_v) > costo(s_a): devolver s_v
#   exp = (costo(s_v) - costo(s_a))/T
#   si r < e^(exp), siendo r un num aleatorio entre 0 y 1:
#       devolver s_v
#   devolver s_a

import math
import random
def esFrontera(u,v,sActual):
    if sActual[u] != sActual[v]:
        return True
    return False
def costoFrontera(sActual:list[int],E):
    costoActual = 0
    for e in range(len(E)):
        if esFrontera(E[e][0],E[e][1],sActual):
            costoActual += costo[e]
    return costoActual
def vecinos(sActual:list[int])->list[list[int]]:
    listaVecinos = []
    for i in range(len(sActual)):
        vecino1 = sActual.copy()
        vecino1[i] = 1 - sActual[i]
        for j in range(i+1,len(sActual)):
            vecino2 = vecino1.copy()
            vecino2[j] = 1 - vecino1[j]
            listaVecinos.append(vecino2)
    return listaVecinos
def particionUniformeAnnealing(V:list[int],E:list[tuple[int,int]], costo:list[int], 
                            maxIt:int, T:float, c:float)->list[int]:
    def costoFrontera(sActual:list[int]):
        costoActual = 0
        for e in range(len(E)):
            if esFrontera(E[e][0],E[e][1],sActual):
                costoActual += costo[e]
        return costoActual
    def proximoEstado(sActual:list[int], sVecino:list[int], T)->list[int]:
        if costoFrontera(sVecino) > costoFrontera(sActual):
            return sVecino
        exp = (costoFrontera(sVecino) - costoFrontera(sActual))/T
        if random.uniform(0,1) < math.e**exp:
            return sVecino
        return sActual
    sActual:list[int] = [0]*len(V)
    sMejor:list[int] = [0]*len(V)
    it=0
    while it < maxIt:
        sVecino = random.choice(vecinos(sActual))
        print(sVecino,costoFrontera(sVecino))
        sActual = proximoEstado(sActual,sVecino,T)
        sMejor = max([sActual,sMejor], key= lambda s: costoFrontera(s))
        T=T*c
        it+=1
    return sMejor
V=[x for x in range(3)]
E=[(0,1),(1,2),(2,1)]
costo=[3,2,1]
esperado = [0, 1, 0]# o [1,0,1]
print("solucion:",particionUniformeAnnealing(V,E,costo,5,1,0.99))
V = list(range(10))
E = [
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 5), (1, 6),
    (2, 3), (2, 6), (2, 7),
    (3, 4), (3, 7), (3, 8),
    (4, 8), (4, 9),
    (5, 6), (5, 7),
    (6, 7), (6, 8),
    (7, 8), (7, 9),
    (8, 9)
]
costo = [
    12, 3, 8, 15,
    7, 11, 4,
    9, 6, 14,
    5, 13, 2,
    10, 16,
    8, 3,
    12, 7,
    5, 11, 4
]
solucion=particionUniformeAnnealing(V,E,costo,50,5,0.5)
print("solucion:",solucion,"costo:", costoFrontera(solucion,E))