# 12. El problema de set independiente corresponde a la clase NP-C. No obstante. Dado la
# gran cantidad de aplicaciones de este, nos interesaría contar con algún mecanismo para
# obtener, dado un grafo G=(V,E), el subconjunto de vértices independientes de mayor tamaño
# posible.
# Acotamos el problema a un grafo con n vértices, donde cada uno de ellos tiene exactamente
# "d" ejes. Analizar el siguiente algoritmo randomizado:
# para cada vértice i seleccionar de forma uniformemente 
# aleatoria xi el valor 0 o 1. Seleccionar para el set 
# independiente únicamente aquellos vértices con el valor 1 que
# no se conecten mediante ejes con otros vértices que tengan el valor 1
# Probar que el set resultante es independiente.
# b) calcular el tamaño esperado del set independiente, en funcion de n y d
# c) Para el cálculo de xi utilizamos p=1/2. 
# Determinar si este es el valor mas conveniente o podemos 
# encontrar uno mejor. Si es así, de la fórmula del valor 
# esperado con esta nueva probabildad.

# p(elegir v) = p(v=1)*p(Todo vertice adyacente a v = 0) = 1/2 * p(vertice = 0)^d = (1/2) * (1/2)^d
# -> (1/2)^(d+1)
# tamaño promedio: N * p(elegir v) -> N * (1/2)^(d+1)
# podemos reescribir el tamaño promedio a N * p(v=1) * p(v=0)^d -> N * p(v=1) * ((1-p(v=1))^d)
# queremos maximizar tamaño tocando solamente la posibilidad de xi=1. solo nos interesa                 
# p(v=1) * ((1-p(v=1))^d)-> a mayor p(xi=1), p(v=1) crece, y ((1-p(v=1))^d) decrece
# ej: n=4, d=2, p(xi=1)=1/3 -> p(v=1) = 1/3, ((1-p(v=1))^d) = (2/3)^2 -> 4/9
# juntando todo: 4 * 1/3 * 4/9 = 16/27 > 1/2
# vs n=4, d=2, P(xi=1)=1/2 -> 4 * 1/2 * (1/2)^2 -> 4 * 1/2 * 1/4 -> 1/2
# vs n=4, d=2, p(xi=1)=2/3 -> 4 * 2/3 * (1/3)^2 -> 8/27 < 1/2
# en gneral: f(x,d)=x*(1-x)^d. queremos derivada en 0 para maximo/minimo local.
# Si derivamos con respecto a x: (1-x)-x*d*(1-x)^(d-1)
# para f(x,1)->f'(x,1)=1-x-x*1*1->1-2x=0 => x=1/2
# para f(x,2)->f'(x,2)=3x^2-4x+1=0->x=1/3
# en general, x= 1/(d+1)