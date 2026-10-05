# 8. Contamos con una carretera de longitud M km que tiene distribuidos varios 
# carteles publicitarios. Cada cartel ”i” está ubicado en un “ki” kilómetro 
# determinado (pueden ubicarse en cualquier posición o fracción de kilómetro) 
# y a quien lo utiliza le asegura una ganancia “gi”. Por una regulación no se 
# puede contratar más de 1 cartel a 5km de otros. Queremos determinar qué carteles 
# conviene contratar de tal forma de maximizar la ganancia a obtener

# Un cartel no puede estar a menos de 5 km de otro.
# Hay tres opciones. Los carteles óptimos hasta un Ki serán:
# 1. los que eram optimos hasta i-1 sin i 
# 2. los que eram optimos hasta i-1 con i
# 3. i 
# maximaGanancia(k) = max(maximaGanancia(k-1)+g(k), maximaGanancia(k-1), g(k))
# sea carteles una lista ordenada ascendente por kilometro de los carteles.
# sea k un diccionario con los kilometros, tal que k[i] nos de la ganancia de i
# sea g un diccionario de las ganancias, tal que g[i] nos de la ganancia de i
# def maximaGanancia(carteles,g,k,i) 
#  si i < 0
#       devolver 0
#  si i >= largo de carteles:
#       devolver maximaGanancia(carteles,g,k,i-1)
#  gananciaExcluido = maximaGanancia(carteles,g,k,i-1)
#  si k no esta a menos de 5km de otro en gananciaExcluido
#       gananciaIncluido = gananciaExcluido + g(i)
#  sino
#       gananciaIncluido = 0
#  devolver maximo(gananciaExcluido, gananciaIncluido, g(i))
VALOR = 0
ELECCION = 1
def maximaGanancia(carteles,g,k,i=None,calculados={}): 
    def puedeEstar(i, elegidos):
        if elegidos == []:
            return True
        print("en i:",i,"y elegidos",elegidos)
        return k[i] - 5 > k[elegidos[-1]]
    def cartelCompatible(i):
        for j in range(i,-1,-1):
            if k[j] < k[i]-5:
                print("cartel compatible para",i,":",j)
                return j
        return -1
    if i == None: 
        i=len(carteles)-1
    if i < 0: 
        return 0, []
    if calculados.get(i) != None: 
        return calculados[i][VALOR],calculados[i][ELECCION]
    gananciaAnterior, elegidosAnterior = maximaGanancia(carteles,g,k,i-1,calculados)
    gananciaSolo = g[i]
    gananciaCompatible, elegidosCompatible = maximaGanancia(carteles,g,k,
                                            cartelCompatible(i),calculados)
    gananciaCompatible += g[i]
    maxima = max(gananciaAnterior, gananciaSolo, gananciaCompatible)
    if maxima == gananciaAnterior:
        print("adentro de excluido") 
        calculados[i] = (gananciaAnterior, elegidosAnterior)
    elif maxima == gananciaSolo: 
        print("adentro de solo") 
        calculados[i] = (gananciaSolo, [i])
    elif maxima == gananciaCompatible:
        print("adentro de compatible")
        nuevo = elegidosCompatible.copy()
        nuevo.append(i)
        calculados[i] = (gananciaCompatible, nuevo)
    print("i:",i,calculados[i][VALOR],calculados[i][ELECCION])
    return calculados[i][VALOR],calculados[i][ELECCION]
g = {0:1,1:2,2:1,3:4,4:1,5:3}
k = {0:1,1:6,2:7,3:8,4:11,5:13}
carteles = [0,1,2,3,4,5]
calculados = {}
ganancia, elegidos = maximaGanancia(carteles, g, k,None, calculados)
print("ganancia",ganancia)
print("elegidos",elegidos)

print("calculados",calculados)