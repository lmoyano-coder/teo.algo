# 24. Contamos una mazo de cartas numeradas del 1 al “n” mezcladas en un orden
# desconocido y boca abajo (no vemos que numero tienen). No podemos modificar ese orden
# ni espiarlo. Debemos iterativamente tomar la carta superior, darla vuelta y apilarla. Una
# carta puede formar una pila nueva o ubicarse en una existente. Para ubicarla en una
# existente debe ser menor a la carta superior de esa pila. Una vez ubicada la carta, no se
# puede mover y pasa a ser la carta superior. El objetivo es ubicar todas las cartas en la menor
# cantidad de pilas. Presentar un algoritmo greedy para resolver el problema.
# heuristica:
# 1. apilar en una pila, y si no se puede, hacer otra. la eleccion de pila es en orden de creacion
# 2. apilar en la pila que mas cerca este de la cart revelada, crear otra si no se puede.
# 
#
#
#
#
#
#
#
#




lista =[]
for i in range(1,52):
    lista.append(i)
print(lista)