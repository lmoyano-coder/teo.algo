# 2. Dado un Grafo dirigido, acíclico G(V, E) con pesos en sus aristas y 
# dos vértices “s” y “t”;
# queremos encontrar el camino de mayor peso que exista entre “s” y “t”. 
# Resolver mediante programación dinámica.

# El camino de mayor peso será: (s->n).MaxPeso + (n->t).Peso, siendo n uno de los nodos
# que tiene un camino hacía t. El camino de mayor peso para n: 
# (s->n-1).MaxPeso + (n-1->n).Peso. Con n-1 uno de los nodos que va hacia n. Y así
# sucesivamente hasta s->s que es 0. Entonces:
# MaxPeso(s->n) = max(for n-1 con camino a n: MaxPeso(s->n-1)) + Peso(n-1->n)
INICIO = 0
FIN = 1
PESO = 2
def maxPeso(grafo, source, destino, memo={},caminoElegido={}):
    if destino == source:
        return 0
    def obtenerCaminos(destino):
        caminos = []
        for camino in grafo:
            if camino[FIN] == destino:
                caminos.append(camino)
        return caminos
    if memo.get(destino) != None:
        return memo.get(destino)
    caminos = obtenerCaminos(destino)
    # pesos = [maxPeso(grafo, source, camino[INICIO], memo) + camino[PESO] 
    #             for camino in caminos]#camino es una arista
    mayorPeso = 0
    anterior = None
    for camino in caminos:
        peso = maxPeso(grafo,source,camino[INICIO],memo,caminoElegido) + camino[PESO]
        if peso > mayorPeso:
            mayorPeso = peso
            anterior = camino
    memo[destino] = mayorPeso
    caminoElegido[destino] = anterior
    print(memo, caminoElegido)
    return memo[destino]
def reconstruir_camino(source, destino, caminoElegido):
    actual = caminoElegido[destino]
    camino = [actual[FIN]]
    while actual != source:
        if actual[INICIO] == source:
            camino.append(actual[INICIO])
            return camino
        actual = caminoElegido[actual[INICIO]]
        camino.append(actual[FIN])
    return camino
memo = {}
grafo = [[0,1,2],[0,2,3],[1,2,2],[2,3,3],[1,4,1],[4,3,1]]#5 nodos
caminoElegido = {}
peso_max = maxPeso(grafo, 0, 3, memo, caminoElegido)
print("peso_max",peso_max)
print("memo",memo)
print("caminoElegido",caminoElegido)
print("reconstruir camino:", reconstruir_camino(0,3,caminoElegido))