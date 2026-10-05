# 19. Dada una matriz booleana de n x m queremos encontrar la mayor submatriz 
# cuadrada cuyos elementos sean sólo “true”. Diseñar un algoritmo 
# mediante programación dinámica para resolverlo.

# la matriz cuadrada de true más grande si solo considero hasta una celda c [0->n*m-1] 
# 1. c es la esquina inferior derecha del cuadrado más grande
# 2. es otra, a la que la celda anterior 'apuntara'
# Dada una matriz mxn llamada M: 
# cuadradoTrue(M,c) = max(calculoCuadrado(c),cuadradoTrue(M,c-1))
# guardare en un diccionario memo el cuadrado al que es esquina una determinada c
# entonces para calcularCuadrado, solo tengo que obtener el lado del cuadrado que
# forma la celda que esta en diagonal a c en la matriz:
# |t t f|
# |t t t| la celda 4 le pide a la celda 1
# |f f f|
# y luego revisar si los lados tambien son true.
# oseas calcularCuadrado es O(n), y si ya se que 
# calcularCuadrado(cDiagonal)+1 < cuadradoTrue(M,c-1), ni siquiera lo calculo
