OUT = 'out'
FUENTE = 'fuente'
SUMIDERO = 'sumidero'
ID = 0
ESPECTADORES = 1
INICIO = 0
FIN = 1
CAPACIDAD = 2
g_guardada = None
f_guardada = None

def construir_gr(g, f):
    gr= g.copy()
    for i in range(len(f)):#los que tienen flujo mayor a 0
        if f[i]<=0:
            continue
        fila = g[i].copy()
        fila[INICIO],fila[FIN] = fila[FIN],fila[INICIO]
        gr.append(fila)
    return gr
def es_adelante(e,f):
    return e <= len(f)-1
def capacidad_restante(e, g, f):
    if not es_adelante(e,f):
        return g[e][CAPACIDAD]
    return g[e][CAPACIDAD] - f[e]
def proximo_camino(gr, f, g):
    def destino_en_camino(candidato, camino):
        for e in camino:
            if gr[e][INICIO] == gr[candidato][FIN]:
                return True
        return False
    def candidato_valido(candidato,gr,f,camino):
        if capacidad_restante(candidato, gr, f) > 0:
            if not destino_en_camino(candidato, camino):
                return True
        return False
    def dfs(gr, nodoActual,camino):
        for candidato in range(len(gr)):
            if gr[candidato][INICIO] != nodoActual:
                continue
            if gr[candidato][FIN] == SUMIDERO:
                if candidato_valido(candidato,gr,f,camino):
                    camino.append(candidato)
                    return camino
            if candidato_valido(candidato,gr,f,camino):
                camino.append(candidato)
                nuevoCamino = dfs(gr, gr[candidato][FIN], camino)
                if nuevoCamino == None or nuevoCamino == []:
                    camino.pop()
                else:
                    return nuevoCamino
        return None
    camino = []
    nodoActual = FUENTE
    camino = dfs(gr, nodoActual, camino)
    return camino
def aumentar_flujo_camino(camino, f, g, gr):
    def e_inversa(e, g):
        for numArista, arista in enumerate(g):
            if arista[INICIO] == gr[e][FIN] and arista[FIN] == gr[e][INICIO]:
                return numArista
        raise Exception("No se encontro e'=(v,u) en e_inversa")
    cuelloBotella = min(camino, key = lambda e: capacidad_restante(e, gr, f))
    cuelloBotella = capacidad_restante(cuelloBotella, g, f)
    for e in camino:
        if es_adelante(e,f):
            f[e] += cuelloBotella
        else:
            f[e_inversa(e,g)] -= cuelloBotella
def ford_fulkerson_dinic(g, f=None):
    if f == None: 
        f = [0]*len(g)
    gr = construir_gr(g,f)
    camino = proximo_camino(gr, f, g)
    while camino != [] and camino != None:
        aumentar_flujo_camino(camino, f, g, gr)
        gr = construir_gr(g,f)
        camino = proximo_camino(gr, f, g)
    # for i in range(len(f)):
    #     print(g[i],f[i],end=",")
    return f
def id_compatibles(lista, idBuscado, comparar=1,devolver=0):
    return [x[devolver] for x in lista if x[comparar] == idBuscado]
def buscar_nodo(lista, nodo):
    for i in lista:
        if i[ID] == nodo:
            return i
    raise Exception('no se encontro el nodo')
def compatibles(listaDondeBuscar, listaId):
    return [buscar_nodo(listaDondeBuscar, i) for i in listaId]
def crear_grafo(bandas, servidores,plataformas, banda_servidor,servidor_plataforma):
    grafo = []
    for b in bandas:
        grafo.append([FUENTE, b[ID], b[ESPECTADORES]])
    for jin in servidores:
        bandas_compatibles = compatibles(bandas,id_compatibles(banda_servidor,jin[ID]))
        for b in bandas_compatibles:
            grafo.append([b[ID], jin[ID], b[ESPECTADORES]])
        grafo.append([jin[ID], jin[ID]+OUT, jin[ESPECTADORES]])
    for p in plataformas:
        servidores_compatibles=compatibles(servidores, id_compatibles(servidor_plataforma,p[ID]))
        for jout in servidores_compatibles:
            grafo.append([jout[ID]+OUT,p[ID],jout[ESPECTADORES]])
        grafo.append([p[ID],SUMIDERO,p[ESPECTADORES]])
    return grafo
def aristasFlujoPositivo(grafo, flujo, idBuscada):
    validosYcompatibles = []
    for e in range(len(grafo)):
        if grafo[e][INICIO] == idBuscada and flujo[e] > 0:
            validosYcompatibles.append(e)
    return validosYcompatibles

def banda_plataforma(grafo, f):
        def existe_en_BP(BP,objetivo):
            for e in BP:
                if e[INICIO] == objetivo[INICIO] and e[FIN] == objetivo[FIN]:
                    return True
            return False
        def obtener_objetivo_BP(BP,objetivo):
            for e in BP:
                if e[INICIO] == objetivo[INICIO] and e[FIN] == objetivo[FIN]:
                    return e
            raise Exception
        flujo = f.copy()
        BP = []
        ENVIADO = 2
        bandas = [[e[FIN],e[CAPACIDAD]] for e in grafo if e[INICIO]==FUENTE]
        for banda in bandas:
            cantidadEspectadores = banda[ESPECTADORES]
            servidoresCompatibles = aristasFlujoPositivo(grafo, flujo, banda[ID])
            for e in servidoresCompatibles:
                plataformasCompatibles = aristasFlujoPositivo(grafo, flujo, grafo[e][FIN]+OUT)
                for ePlataforma in plataformasCompatibles:
                    if cantidadEspectadores <= 0:
                        break
                    objetivo = [banda[ID],grafo[ePlataforma][FIN],0]
                    if not existe_en_BP(BP, objetivo):
                        BP.append(objetivo)
                    bandaPlataforma = obtener_objetivo_BP(BP, objetivo)
                    cambio = min(flujo[ePlataforma],cantidadEspectadores,flujo[e])
                    bandaPlataforma[ENVIADO] += cambio
                    cantidadEspectadores -= cambio
                    flujo[ePlataforma] -=  cambio
        return BP

def desplegar_espectadores(G, flujo):
    flujoMax = sum([flujo[e] for e in range(len(G)) if G[e][FIN] == SUMIDERO])
    espectadores_requeridos = sum([e[CAPACIDAD] for e in G if e[INICIO] == FUENTE])
    posible = flujoMax == espectadores_requeridos
    asignaciones = banda_plataforma(G, flujo)
    return posible, flujoMax, asignaciones

def main(bandas:list[tuple[str,int]], servidores:list[tuple[str,int]], 
        plataformas:list[tuple[str,int]], banda_servidor:list[tuple[str,str]],
        servidor_plataforma:list[tuple[str,str]]):
    global g_guardada, f_guardada
    G:list = crear_grafo(bandas, servidores,plataformas, banda_servidor,servidor_plataforma)
    flujo:list = ford_fulkerson_dinic(G)
    g_guardada, f_guardada = G, flujo
    return desplegar_espectadores(G, flujo)

def equilibrar(g, f, vertice, cola):
    def conjuntoYFlujo(g, direccion, vertice):
        conjunto = [e for e in range(len(g)) if g[e][direccion] == vertice]
        flujo = sum([f[e] for e in conjunto])
        return conjunto, flujo
    # Conservación del flujo: en cada vértice intermedio, el flujo que entra debe ser igual al que sale
    if vertice == FUENTE or vertice ==SUMIDERO:
        return
    anteriores, flujoAnteriores = conjuntoYFlujo(g, FIN, vertice)#los que terminan en vertice
    siguientes,flujoSiguientes = conjuntoYFlujo(g, INICIO, vertice)#los que empiezan en vertice
    if flujoAnteriores == flujoSiguientes:
        return
    excedido = siguientes if flujoSiguientes > flujoAnteriores else anteriores
    direccion = FIN if flujoSiguientes > flujoAnteriores else INICIO
    exceso = abs(flujoAnteriores - flujoSiguientes)
    for e in excedido:
        if exceso <= 0:
            break
        cambio = min(f[e], exceso)
        f[e] -= cambio
        exceso -= cambio
        cola.append(g[e][direccion])

def bfs_equilibrar(g, f, id_servidor):
    cola = [id_servidor,id_servidor+OUT]
    for vertice in cola:
        equilibrar(g, f, vertice, cola)

def actualizar_servidor(id_servidor: str, nueva_capacidad: int):
    def obtener_objetivo(lista,objetivo):
        for e in range(len(lista)):
            if lista[e][INICIO] == objetivo[INICIO] and lista[e][FIN] == objetivo[FIN]:
                return e
        raise Exception
    global g_guardada, f_guardada
    if g_guardada == None or f_guardada == None:
        raise Exception("ERROR: Se debe llamar a main previamente")
    
    aristaServidor = obtener_objetivo(g_guardada,[id_servidor, id_servidor+OUT])

    if nueva_capacidad >= g_guardada[aristaServidor][CAPACIDAD]:
        g_guardada[aristaServidor][CAPACIDAD] = nueva_capacidad
        return desplegar_espectadores(g_guardada, f_guardada)
    
    g_guardada[aristaServidor][CAPACIDAD] = nueva_capacidad
    f_guardada[aristaServidor] = nueva_capacidad

    bfs_equilibrar(g_guardada,f_guardada,id_servidor)
    return desplegar_espectadores(g_guardada, f_guardada)

bandas = [("B1", 6), ("B2", 4)]
servidores = [("S1", 5), ("S2", 6)]
plataformas = [("P1", 5), ("P2", 5)]
bs = [("B1", "S1"), ("B1", "S2"), ("B2", "S2")]
sp = [("S1", "P1"), ("S2", "P1"), ("S2", "P2")]
asignacionEsperada = [['B1', 'P1', 5], ['B1', 'P2', 1], ['B2', 'P2', 4]]

print(main(bandas, servidores, plataformas, bs, sp))
print("---------")
print(actualizar_servidor("S2",4))

# print(g_guardada, f_guardada)
# print(posible, flujo_max, asignacion)


# g = [['fuente','2',10],['fuente','1',20],['2','3',10],['1','3',30],
#                     ['1','4',10],['3','sumidero',20],['4','sumidero',10]]
# f = ford_fulkerson_dinic(g)
# print(f)