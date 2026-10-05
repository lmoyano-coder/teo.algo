# 16. Se conoce como “Longest increasing subsequences” al problema de, 
# dado un vector de numérico, encontrar la subsecuencia más larga de números 
# (no necesariamente consecutivos) donde cada elemento sea mayor a los anteriores. 
# Ejemplo: En la lista → 2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7. Podemos ver que la 
# subsecuencia más larga es de longitud 6 y corresponde a la siguiente 
# “1, 2, 3, 4, 6, 7”. Resolver el problema mediante programación dinámica.

# para un i del vector v, reviso el masLarga(v,x) de todos los x anteriores a i
# y si v[x] < v[i] le sumo 1. Guardare el más largo que incluya a i en memo[i]
# candidatos = [masLarga(v,x) por range(0,i) y v[x] < v[i]]
# return max(candidatos)+1