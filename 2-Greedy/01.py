# 1. Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado
# (ordenado por nombre del pueblo) contiene el número de kilómetros donde está ubicada
# cada una. Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) de
# tal forma que no haya bifurcaciones con vigilancia a más de 50 km. Proponer un algoritmo
# que lo resuelva
# pueblos = ('bahia blanca', 10) ('san martin de los ande', 110) ('la plata', 70) ('caba', 50)
# posibles criterios greedy optimos:
# 1. donde hay mas interseccion de bifurcasiones(la primera si hay varias)
# 2. la primera que aparece(que no esta ya cubierta)
# 3. la ultima que aparece(que no esta cubierta)
# 4. donde hay menor interseccion de bifurcaciones
# 2. descarto, contra ejemplo: ("a",0) ("b", 30) ("c", 50). Selecciona a, pero lo optimo es b
# 3. descarto, idem ejemplo de antes.
# 4. descarto, contra ejemplo: ("a",0) ("b", 30) ("c", 50) ("d", 60). 
# Selecciona a, pero lo optimo es b
# 1. no tiene contra ejemplo obvio, lo voy a implementar

nombre = 0
posicion = 1

def esta_cerca(pivote, candidato):
    return (pivote - 50 <= candidato and pivote + 50 >= candidato)
def pueblos_no_cubiertos(pueblos, patrullas):
    no_cubiertos = pueblos.copy()
    for p in patrullas:
        for pueblo in pueblos:
            if esta_cerca(p, pueblo[posicion]):
                no_cubiertos.remove(pueblo)
    return no_cubiertos
def contar_interseccion(pueblos):
    if pueblos == []:
        return []
    intersecciones = {}
    for pivote in pueblos:
        intersecciones[pivote] = 0
        for candidato in pueblos:
            if candidato == pivote:
                continue
            if esta_cerca(pivote[posicion], candidato[posicion]):
                intersecciones[pivote] += 1
    return intersecciones
def promedio_dist(pueblos):
    total = 0
    for i in pueblos:
        total += pueblos[i]
    return total / len(pueblos)
def menor_patrullas(pueblos):#O(n^3) o O(n^2) si se implementa mejor
    patrullas = []
    pueblos_restantes = pueblos.copy()
    while len(pueblos_no_cubiertos(pueblos_restantes, patrullas)) != 0:#n
        pueblos_restantes = pueblos_no_cubiertos(pueblos_restantes, patrullas)#n^2,puede hacerse con n
        inter = contar_interseccion(pueblos_restantes)#n^2, puede hacerse con n
        mas_inter = max(inter, key=lambda pueblo: inter[pueblo])#n
        patrullas.append(mas_inter[posicion])
    return patrullas
pueblos1 = [("a",0), ("b", 30), ("c", 50), ("d", 60)]
print(menor_patrullas(pueblos1))
pueblos2 = [('bahia blanca', 10), ('san martin de los ande', 110), ('la plata', 70), ('caba', 50)]
print(menor_patrullas(pueblos2))
pueblos3 = [("a",0), ("b", 30), ("c", 50), ("d", 60),("e",-20), ("f", 200), ("g", 150), ("h", 160)]
print(menor_patrullas(pueblos3))
pueblos4 = [("a",0), ("b", 40), ("c", 60), ("d", 100),("e",100), ("f", 120)]
print(menor_patrullas(pueblos4))#fallo, optimo es (40, 100)

# no_cubiertos1 = pueblos_no_cubiertos(pueblos1, [30])
# print("pueblos1: ", pueblos1, "patrullas en: ", [30])
# print(no_cubiertos1)
# no_cubiertos2 = pueblos_no_cubiertos(pueblos2, [10, 200])
# print("pueblos2: ", pueblos2, "patrullas en: ", [10, 200])
# print(no_cubiertos2)
# print(contar_interseccion(pueblos1))
# inter2 = contar_interseccion(pueblos2)
# print(inter2)
# print(max(inter2, key=lambda pueblo: inter2[pueblo]))
