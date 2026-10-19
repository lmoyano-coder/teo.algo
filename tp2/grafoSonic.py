# La transmisión de este año es: 
# bandas KUNAI (7), VÖLSA (5) y TREMOR (6); 
# servidores ZARZA (8), MIRLO (7) y OTEO (5); 
# plataformas ONDA (10) y CRISOL (8). 
# KUNAI se transmite por ZARZA y MIRLO, VÖLSA por MIRLO y OTEO, y TREMOR por ZARZA y 
# OTEO; ZARZA llega a ONDA, MIRLO a ONDA y CRISOL, y OTEO a CRISOL. 
OUT = 'out'
FUENTE = 'fuente'
SUMIDERO = 'sumidero'
ID = 0
ESPECTADORES = 1
INICIO = 0
FIN = 1
CAPACIDAD = 2
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
def ford_fulkerson_dinic(g):
    f = [0]*len(g)
    gr = construir_gr(g,f)
    camino = proximo_camino(gr, f, g)
    while camino != [] and camino != None:
        aumentar_flujo_camino(camino, f, g, gr)
        gr = construir_gr(g,f)
        camino = proximo_camino(gr, f, g)
    for i in range(len(f)):
        print(g[i],f[i],end=",")
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
def banda_plataforma(grafo, f, bandas):
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
                    cambio = min(flujo[ePlataforma],cantidadEspectadores)
                    bandaPlataforma[ENVIADO] += cambio
                    cantidadEspectadores -= cambio
                    flujo[ePlataforma] -=  cambio
        return BP
def main(bandas:list[tuple[str,int]], servidores:list[tuple[str,int]], 
        plataformas:list[tuple[str,int]], banda_servidor:list[tuple[str,str]],
        servidor_plataforma:list[tuple[str,str]]):
    def desplegar_espectadores():
        G:list = crear_grafo(bandas, servidores,plataformas, banda_servidor,servidor_plataforma)
        flujo:list = ford_fulkerson_dinic(G)
        flujoMax = sum([flujo[e] for e in range(len(G)) if G[e][FIN] == SUMIDERO])
        espectadores_requeridos = sum([e[CAPACIDAD] for e in G if e[INICIO] == FUENTE])
        posible = flujoMax == espectadores_requeridos
        asignaciones = banda_plataforma(G, flujo, bandas)
        return posible, flujoMax, asignaciones
    return desplegar_espectadores()

bandas = [('KUNAI',7),('VÖLSA',5),('TREMOR',6)]
servidores = [('ZARZA',8),('MIRLO',7),('OTEO',5)]
plataformas = [('ONDA',10),('CRISOL',8)]
bs = [('KUNAI','ZARZA'),('KUNAI','MIRLO'),('VÖLSA','MIRLO'),
                    ('VÖLSA','OTEO'),('TREMOR','ZARZA'),('TREMOR','OTEO')]
sp = [('ZARZA','ONDA'),('MIRLO','ONDA'),('MIRLO','CRISOL'),
                    ('OTEO','CRISOL')]

posible, flujo_max, asignacion = main(bandas, servidores, plataformas, bs, sp)
print("\n",posible, flujo_max, asignacion)


# g = [['fuente','2',10],['fuente','1',20],['2','3',10],['1','3',30],
#                     ['1','4',10],['3','sumidero',20],['4','sumidero',10]]
# f = ford_fulkerson_dinic(g)
# print(f)