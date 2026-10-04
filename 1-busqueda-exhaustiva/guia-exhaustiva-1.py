# 1. Contamos con un conjunto de “n” puntos (x,y) en el plano cartesiano. Un par de
# puntos es el más cercano si la distancia euclidiana entre ellos es menor a la de cualquier
# otro par. Resuelva el problema mediante un algoritmo naive que nos informe cuales son
# los 3 pares de puntos más cercanos
import math
def tres_pares_cercanos(puntos:list):
    def distancia(p1, p2):
        resto = [p1[0] - p2[0],p1[1] - p2[1]]
        return math.sqrt(resto[0]**2 + resto[1]**2)
    if puntos == []:
        return []
    lista_puntos_cercanos = []
    indice = -1
    for indice, punto_pivote in enumerate(puntos):
        candidato_menor = None
        distancia_menor = None
        for j, punto_cercano_candidato in enumerate(puntos):
            if indice == j:
                continue
            distancia_nueva = distancia(punto_pivote, punto_cercano_candidato)
            if distancia_menor == None or distancia_nueva < distancia_menor:
                candidato_menor = punto_cercano_candidato
                distancia_menor = distancia_nueva
        lista_puntos_cercanos.append([punto_pivote, candidato_menor])
    return sorted(lista_puntos_cercanos)[:3]

puntos = [[0,0],[10,1],[3,0],[0,-1]]
print("los tres pares mas cercanos: ",tres_pares_cercanos(puntos))