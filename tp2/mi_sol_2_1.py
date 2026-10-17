# función que cuenta las permutaciones debe llamarse contar_avenidas 
# y la tabla de programación dinámica, visibles_por_prefijo.
# matriz de memoización: memo[elemento,posicion]->permutaciones
# El n-esimo elemento (el más grande) siempre será visible.
# el n-1 elemento será visible solo si esta adelante de n, y asi sucesivamente
# esto quiere decir que si quiero k torres visibles, n debe estar como mucho en k-1
# las permutaciones serán las sumas de n en k, k+1,...,n-1,n

# 1 2 3 4, selecciono 2:



# 3 4 1 2
# 3 4 2 1
# 3 1 4 2
# 3 2 4 1
# 3 1 2 4
# 3 2 1 4
# 2 4 1 3
# 2 4 3 1
# 2 1 4 3
# 1 4 2 3
# 1 4 3 2

# total = 11

# 1 2 3 4, 3 visibles:

# 1 2 4 3
# 1 3 4 2
# 1 3 2 4
# 2 3 4 1
# 2 3 1 4
# 2 1 3 4

# 1 2 3 4 5 6, visible 5

# 1 3 2 4 5 6
# 2 3 1 4 5 6
# 2 1 3 4 5 6
# 1 3 4 2 5 6
# 2 3 4 1 5 6
# 1 2 4 3 5 6
# 1 3 4 5 2 6
# 2 3 4 5 1 6
# 1 2 3 5 4 6
# 1 2 4 5 3 6
# 1 2 4 5 6 3
# 1 2 3 5 6 4
# 1 3 4 5 6 2
# 2 3 4 5 6 1
# 1 2 3 4 6 5



#-----------------------------

# recurrencia eduardo: torres(n, k) = torres(n-1,k)*n+torres(n-1,k-1)