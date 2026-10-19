# 2. Problema del camino más largo en un grafo general con aristas sin peso: Dados G = (V, E)
# un grafo no dirigido y un natural k, determinar si existe un camino simple en G de longitud
# >=k. Probar que es un problema NP-completo (Usar el problema del camino hamiltoniano
# para probarlo).

# queremos probar que Ch(>=p)Cl y que Cl pertenece a P. Es decir, que el problema del 
# camino hamiltoniano puede ser reducido polinomialmente al problema del camino más largo.
# y que el problema del camino más largo pertenece a P 
# (existe un algoritmo que chequee solucion en tiempo polinomial). Si se cumplen ambas podemos 
# asegurar NP-C

# queremos transformar de alguna manera el input de Ch en tiempo polinomial, y darselo a Cl
# no sabemos como lo solucionara Cl, solo que lo hara, es decir es una caja negra.
# en el problema del camino hamiltoneano, queremos saber si para un grafo dirigido o no existe
# un camino que pase por todos los vertices una solo vez. Es decir, que si tiene m vertices,
# queremos que haga un recorrido de largo m. El problema del camino más largo nos dice si para
# un determinado grafo, existe un camino simple(no se repiten vertices) de largo >= k.
# si tenemos m vertices, el camino más largo será como mucho m, ya que si fuera más grande
# estaríamos repitiendo vertices, lo cual está prohíbido.
# Entonces, si le doy el grafo de Ch a Cl, con un k = cantidad de vertices del grafo pasado
# Cl nos devolverá si un camino con largo >= k, pero como el largo de un camino esta acotado:
# cantidad vertices >= largo entonces sigue que: cantidad vertices >=largo>=k entonces:
# y como k y cantidad de vertices son iguales-> k >= largo >= k -> largo = k
# por lo tanto puede reducir polinomicamente Ch en Cl
# ahora necesito probar que pertenece a P
# pseudo codigo:
# sea G = (V, E)
# sea prueba un camino de vertices
# chequeador(G, prueba)
#   si un v de prueba no pertence a G -> devolver falso
#   si un v de G aparece dos veces en prueba -> devolver falso
#   Si para un len(prueba)>i>=1 no existe un e=(prueba[i-1], prueba[i]) perteneciente a G:
#       devolver falso
#   si len(prueba) != cantida vertices de G -> devolver falso

# por tanto Cl es NP-C