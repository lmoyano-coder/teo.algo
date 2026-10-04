# Tenemos un grafo conexo simple, que parte de una fuente infinita a un sumidero infinito.
# Encontrar el flujo maximo y devolver la funcion f (vector que contiene el flujo de cada eje/arista)
# G es un grafo (v,e) que representala capacidad en cada eje/arista mediante matriz arista vertice
def es_adelante(e,f):
    if e <= len(f)-1:#ej g=[[-1,1]],f=[1],len=1,e=0
        return True
    return False
def obtener_vertices(fila:list):
    u, v = None, None
    for i in range(0,len(fila)):
        if fila[i] != 0:
            u = i
            break
    for j in range(u+1, len(fila)):
        if fila[j] != 0:
            v = j
    if u == None or v == None:
        raise Exception("No hay 2 elementos no nulos en la lista")
    return u, v
def invertir_e(e,g):
    u,v = obtener_vertices(g[e])
    for i in range(len(g)):
        ui,vi = obtener_vertices(g[i])
        if ui == u and vi == v:
            return i
    raise Exception("No se encontro e'=(v,u)")
def capacidad(fila):
    for i in fila:
        if i > 0:
            # print("capacida",fila,i)
            return i
    raise Exception("Empty row")
def capacidad_restante(e, G:list[list], f:dict):
    # print("capacidad restante:", capacidad(G[e]),"-", f[e],"=",capacidad(G[e]) - f[e])
    if not es_adelante(e,f):
        return capacidad(G[e])
    return capacidad(G[e]) - f[e]
def aumentar_flujo_camino(p:list, f: list, g:list):
    w = min(p, key = lambda e: capacidad_restante(e, g, f))
    w = capacidad_restante(w, g, f)
    for e in p:
        if es_adelante(e,f):
            f[e] += w
        else:
            e_inversa = invertir_e(e,g)
            f[e_inversa] -= w
def sale_de_u_llega_a_v(u,v):
        if u < 0:
            return u,v
        else: 
            return v,u
def construir_gr(g,f):
    gr= g.copy()
    for i in range(len(f)):#los que tienen flujo mayor a 0
        if f[i]<=0:
            continue
        fila = [0]*len(f)
        u, v = obtener_vertices(g[i])
        u, v = sale_de_u_llega_a_v(u,v)#me aseguro de que el flujo es desde u a v
        fila[u] = -f[i]
        fila[v] = f[i]#es un eje para atras, por lo que sale de manera inversa
        gr.append(fila)
    return gr
def proximo_camino(gr,f):
    def no_v(x,y,v):
        if x==v:
            return y
        return x
    def vertice_disponible(gr, v, camino):
        for i in range(len(gr)):
            if gr[i][v] >= 0:
                continue
            x, y = obtener_vertices(gr[i])
            candidato = no_v(x,y,v)
            if capacidad_restante(i, gr, f) > 0 and candidato not in camino:
                return candidato
        return None
    camino = [0]
    for i in camino:
        v = vertice_disponible(gr, i,camino)
        if v == None:
            return []
        camino.append(v)
        if v == len(gr[0])-1:
            return camino
    return []
def camino_por_ejes(gr, f, camino):
    camino_ejes = []
    for i in range(len(camino)-1):
        for j in range(len(gr)):
            u, v = obtener_vertices(gr[j])
            u, v = sale_de_u_llega_a_v(u,v)
            if v == camino[i] and u == camino[i+1]:
                camino_ejes.append(j)
    return camino_ejes
def flujo_maximo(g,f):
    gr = construir_gr(g,f)
    camino = proximo_camino(gr, f)
    while camino != []:
        print("nuevo ciclo while")
        print("camino:", camino)
        camino_ejes = camino_por_ejes(g, f, camino)
        print("camino_ejes",camino_ejes)
        aumentar_flujo_camino(camino_ejes, f, g)
        print("f:",f)
        gr = construir_gr(g,f)
        camino = proximo_camino(gr, f)
    return f
