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
def main(bandas:list[tuple[str,int]], servidores:list[tuple[str,int]], 
        plataformas:list[tuple[str,int]], banda_servidor:list[tuple[str,str]],
        servidor_plataforma:list[tuple[str,str]]):
    def id_compatibles(lista, idBuscado):
        return [x[INICIO] for x in lista if x[FIN] == idBuscado]
    def buscar_nodo(lista, nodo):
        for i in lista:
            if i[ID] == nodo:
                return i
        raise Exception('no se encontro el nodo')
    def compatibles(listaDondeBuscar, listaId):
        return [buscar_nodo(listaDondeBuscar, i) for i in listaId]
    def crear_grafo():
        grafo = []
        for b in bandas:
            grafo.append([FUENTE, b[ID], b[ESPECTADORES]])
        for jin in servidores:
            id_bandas_compatibles = id_compatibles(banda_servidor,jin[ID])
            bandas_compatibles = compatibles(bandas,id_bandas_compatibles)
            for b in bandas_compatibles:
                grafo.append([b[ID], jin[ID], b[ESPECTADORES]])
            grafo.append([jin[ID], jin[ID]+OUT, jin[ESPECTADORES]])
        for p in plataformas:
            id_servidores_compatibles = id_compatibles(servidor_plataforma,p[ID])
            servidores_compatibles=compatibles(servidores, id_servidores_compatibles)
            for jout in servidores_compatibles:
                grafo.append([jout[ID]+OUT,p[ID],jout[ESPECTADORES]])
            grafo.append([p[ID],SUMIDERO,p[ESPECTADORES]])
        return grafo
    def ford_fulkerson_dinic(G):
        return []
    def banda_plataforma(grafo, flujo):
        pass
    def desplegar_espectadores():
        G:list = crear_grafo()
        flujo:list = ford_fulkerson_dinic(G)
        flujoMax = sum([flujo[e] for e in range(len(G)) if G[e][FIN] == SUMIDERO])
        espectadores_requeridos = sum([e[CAPACIDAD] for e in G if e[INICIO] == FUENTE])
        posible = flujoMax == espectadores_requeridos
        asignaciones = banda_plataforma(G, flujo)
        return posible, flujoMax, asignaciones
        pass

    return crear_grafo()
bandas = [('KUNAI',7),('VÖLSA',5),('TREMOR',6)]
servidores = [('ZARZA',8),('MIRLO',7),('OTEO',5)]
plataformas = [('ONDA',10),('CRISOL',8)]
banda_servidor = [('KUNAI','ZARZA'),('KUNAI','MIRLO'),('VÖLSA','MIRLO'),
                    ('VÖLSA','OTEO'),('TREMOR','ZARZA'),('TREMOR','OTEO')]
servidor_plataforma = [('ZARZA','ONDA'),('MIRLO','ONDA'),('MIRLO','CRISOL'),
                    ('OTEO','CRISOL')]
# bandas KUNAI (7), VÖLSA (5) y TREMOR (6); 
# servidores ZARZA (8), MIRLO (7) y OTEO (5); 
# plataformas ONDA (10) y CRISOL (8). 
# KUNAI se transmite por ZARZA y MIRLO, VÖLSA por MIRLO y OTEO, y TREMOR por ZARZA y 
# OTEO; ZARZA llega a ONDA, MIRLO a ONDA y CRISOL, y OTEO a CRISOL.
print(main(bandas, servidores, plataformas,banda_servidor,servidor_plataforma))

