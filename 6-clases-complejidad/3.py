# 3. La siguiente es una versión de Conjunto Independiente. Dado un grafo G= (V, E) y un
# entero k, decimos que I ⊆ V es fuertemente independiente si dados dos vértices u y v en I, la
# arista (v, u) no pertenece a E y además no hay ningún camino de tamaño 2 (con dos aristas)
# de u a v. El problema de Conjuntos Fuertemente Independientes consiste en decidir si G
# tiene un conjunto fuertemente independiente de tamaño al menos k. Probar que el
# problema de Conjuntos Fuertemente Independientes es NP completo. Utilizar para ello que
# Conjuntos Independientes es NP completo

# idea: por cada arista e=(u,v) voy a reemplazarla por e1=(u,n) y e2=(n,v), siendo n un vertice
# que no pertenece a V, y creando uno por cada arista.