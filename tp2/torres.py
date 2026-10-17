import math

# n = lista de torres; m = cantidad de torres visibles
# asumo que la lista n llega ordenada y que tiene al menos un elemento
# asumo que m es un numero positivo mayor a 0
def torres_visibles(n, m):
    if len(n) < m:
        return 0
    if len(n) == m:
        return 1
    if m == 1:
        return math.factorial(len(n)-1)

    torres = n.copy()
    permutaciones = 0
    torres.pop()

    # "escondo la torre" - la multiplicación es por la cantidad de lugares
    # en los que puedo dejar la torre sin que sea visible
    permutaciones += torres_visibles(torres, m) * len(torres)

    # dejo la torre visible
    permutaciones += torres_visibles(torres, m-1)
    #f(4,2)= f(3,2)*3+f(3,1)->3*3+2!
    #f(3,2)= f(2,2)*2+f(2,1)->1*2+1!
    return permutaciones


# pruebas
torres_1 = [1, 2 ,3 ,4]
torres_2 = [1, 2, 3, 4, 5, 6]
torres_3 = [1]
torres_4 = [1,2]

print(torres_visibles(torres_1, 1))
print(torres_visibles(torres_1, 2))
print(torres_visibles(torres_1, 3))
print(torres_visibles(torres_1, 4))
print(torres_visibles(torres_2, 1))
print(torres_visibles(torres_2, 2))
print(torres_visibles(torres_2, 3))
print(torres_visibles(torres_2, 4))
print(torres_visibles(torres_2, 5))
print(torres_visibles(torres_2, 6))
print(torres_visibles(torres_3, 1))
print(torres_visibles(torres_4, 1))
print(torres_visibles(torres_4, 2))
