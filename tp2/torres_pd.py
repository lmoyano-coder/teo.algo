import math

# Eq de recursion.
# torres_visibles(t,v) = (torres_visibles(t-1,v) * (t-1)) + torres_visibles (t-1,v-1)

# t = numero de torres; v = cantidad que quiero visibles
# asumo que t y v son positivos mayores a 0
def torres_visibles(t, v):
    torres = [[0 for _ in range(v)] for _ in range(t)]

    for i in range(t):
        torres[i][0] = math.factorial(i)
        
        for j in range(1, v):
            torres[i][j] = (torres[i-1][j] * (i)) + torres[i-1][j-1]

    return torres[t-1][v-1]

print("t = 4, v = 1, total = ", torres_visibles(4, 1))
print("t = 4, v = 2, total = ", torres_visibles(4, 2))
print("t = 4, v = 3, total = ", torres_visibles(4, 3))
print("t = 4, v = 4, total = ", torres_visibles(4, 4))
print("t = 4, v = 5, total = ", torres_visibles(4, 5))
print("t = 5, v = 1, total = ", torres_visibles(5, 1))
print("t = 5, v = 2, total = ", torres_visibles(5, 2))
print("t = 5, v = 3, total = ", torres_visibles(5, 3))
print("t = 5, v = 4, total = ", torres_visibles(5, 4))
print("t = 5, v = 5, total = ", torres_visibles(5, 5))
print("t = 5, v = 6, total = ", torres_visibles(5, 6))
print("t = 6, v = 1, total = ", torres_visibles(6, 1))
print("t = 6, v = 2, total = ", torres_visibles(6, 2))
print("t = 6, v = 3, total = ", torres_visibles(6, 3))
print("t = 6, v = 4, total = ", torres_visibles(6, 4))
print("t = 6, v = 5, total = ", torres_visibles(6, 5))
print("t = 6, v = 6, total = ", torres_visibles(6, 6))
print("t = 6, v = 7, total = ", torres_visibles(6, 7))

