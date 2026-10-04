# 4. Contamos con una red de Flujo definida sobre el grafo G=(V,E) y tenemos una
# asignación de flujo f(e) sobre G. Nos solicitan elaborar un algoritmo que en base a esta
# información nos indique cómo se actualiza el flujo si uno de los ejes tiene un cambio de
# capacidad (puede ser positiva o negativa). Debemos evitar volver a ejecutar el algoritmo de
# Ford-Fulkerson desde cero. Explicar los diferentes casos que podrían suceder. Utilizar los
# conceptos de flujo máximo/corte mínimo en su explicación. Brindar pseudocódigo de su
# propuesta y análisis de complejidad.

# Afirmación: Si el nodo x era un cuello de botella para alguno camino de flujo a T (sumidero)
# tal vez cambiara el flujo máximo. Voy a buscar si esto se cumple. 
# (cuello de botella de capacidad restante)
# Armare k caminos, siguiendo las aristas con flujos no nulos
# ej: g=[[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[-1,0,1,0]], x = 2, f= [1,1,1,0], camino=(1->2->3->4)
# Si x es cuello de botella de alguno de los k caminos,(con x+=variacion), el flujo maximo será:
# For x in camino if bottleNeck(camino)==x_original:
#   Si bottleNeck(camino) == x -> flujo_maximo += variacion
#   Si bottleNeck(camino) == y -> flujo_maximo += diferencia(x, y) (x ya tiene sumado variacion):
#       x -= diferencia(x, y) (para si hay otro camino de x que aproveche el cambio restante)
# Como estoy recorriendo los k caminos que tienen como mucho E aristas, tengo complejidad O(E*K)
# mismo para construir caminos: estoy creando K caminos con como mucho E aristas: O(E*K)
