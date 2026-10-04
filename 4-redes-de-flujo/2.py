# 2. La red de transporte intergaláctico es una de las maravillas del nuevo imperio terráqueo.
# Cada tramo de rutas galácticas tiene una capacidad infinita de transporte entre ciertos
# planetas. No obstante, por burocracia - que es algo que no los enorgullece - existen puestos
# de control en cada planeta que reduce cuantos naves espaciales pueden pasar por día por
# ella. Por una catástrofe en el planeta X, la tierra debe enviar la mayor cantidad posible de
# naves de ayuda. Por un arreglo, durante un día los planetas solo procesaran en los puestos
# de control aquellas naves enviadas para esta misión. Tenemos que determinar cuál es la
# cantidad máxima de naves que podemos enviar desde la tierra hasta el planeta X.
# Sugerencia: considerar a este un problema de flujo con capacidad en nodos y no en ejes
# Resolución
# Nos daran un grafo con planetas, que arranca desde la tierra(fuente infinita)
# hasta planeta X(sumidero infinito). Cada 'ruta' entre planetas tiene capacidad infinita.
# Creare un nodo por cada puesto de control (es decir por cada planeta),y lo conectarare con su planeta
# planeta -> puesto de control. La capacidad de el eje será la capacidad de procesar naves del puesto.
# tambien rederigiré las rutas del planeta1 -> planeta2 al puesto, quedaría planeta1->puesto1->planeta2
# La tierra y planeta X no tienen puesto de control(de otro modo no serían infinitos)
# Finalmente aplicamos el algoritmo de flujo maximo
# complejidad temporal: O(2V(E^2))



