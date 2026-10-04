# 3. La compañía eléctrica de un país nos contrata para que le ayudemos a ver si su red de
# transporte desde su nueva generadora hidroeléctrica hasta su ciudad capital es robusta. Nos
# otorgan un plano con la red eléctrica completa: todas las subestaciones de distribución y red
# de cableados de alta tensión. Lo que quieren que le digamos es: cuantas secciones de su red
# se pueden interrumpir antes que la ciudad capital deje de recibir la producción de la
# generadora? (Sugerencia: investigue sobre el Teorema de Menger) Puede informar cual es el
# subconjunto de ejes cuya falla provoca este problema?

# Sea la generadora hidroeléctrica la fuente S, y la capital el sumidero T
# Armo un grafo g con las subestaciones como nodos y los cableados como aristas con capacidad 1.
# Resuelvo por medio de algoritmo de flujo maximo. 
# El flujo que llega al sumidero es la cantidad de secciones de su red que se pueden interrumpir
# antes de que la ciudad deje de recibir electricidad de la generadora.
# Para obtener el subconjunto de ejes, primero genero una gr con g y f. 
# Sea A los nodos alcanzables desde S, y sea B = G - {A} (los que no puedo alcanzar)
# Un corte minimo seran los ejes que conecten los nodos de A->B (notese, NO B->A)
