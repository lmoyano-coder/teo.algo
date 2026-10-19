# 12. Definimos el problema Subgrafo denso de la siguiente manera: Dado un grafo G=(V,E)
# y dos parámetros a y b. Existe en G un subconjunto S de al menos “a” vértices con al menos
# “b” ejes entre ellos. Demostrar que este problema es NP-Completo. Sugerencia: Utilizar el
# problema del Clique

# El problema del clique dice si existe un clique(subgrafo completo) en G de almenos tamaño k.
# Sea G=(V,E) un grafo completo: su catnidad de aristas será: e = (V+(V-1))/2.  
# si clique(G,k) devuelve true, quiere decir que hay un conjunto C \contenidoEn V
# tal que C es completo. Si es completo tendrá n(n-1)/2 aristas y n vertices.
# le pasó a subgrafoDenso(G,k,k(k-1)/2) y si devuelve true hay un subgrafo completo
# de almenso tamaño k