# lista = [1,3,4,6,5]*2
# print("lista completa ", lista)
# print("3 primeros ", lista[:3])
# def generar_matrix_cuadrada(largo:int):
#     matriz = []
#     for i in range(largo):
#         matriz.append([0] * largo)
#     return matriz
# lista_doble = [[0]*8]*8
# lista_doble[0][1] = 2
# matriz_cuadrada = generar_matrix_cuadrada(8)
# matriz_cuadrada[0][1] = 2
# print(lista_doble)
# print(matriz_cuadrada)
# elementos = [1,2,3,4]
# for i, e in enumerate(elementos):
#     if e == 2:
#         del elementos[i]
# print(elementos)
# print(3 in elementos)
# print(10 in elementos)
# elementos.remove(3)
# print(elementos)
# e = [1]
# b = e
# e[0] = 2
# print(e, " ", b)
# import math
# def divisores_de_num(num:int):
#     if (num < 0):
#         return []
#     divisores = [1]
#     for i in range(2, math.ceil(math.sqrt(num))):
#         if num % i == 0:
#             divisores.append(int(i))
#             divisores.append(int(num / i))
#     divisores.append(num)
#     return sorted(divisores)
# print(divisores_de_num(10))
# print(divisores_de_num(12))
# print(divisores_de_num(11))
# print(divisores_de_num(221))
# print(divisores_de_num(38))
# print(divisores_de_num(24))
# print(divisores_de_num(60))
# with open("algo.csv", "r") as archivo:
#     texto = archivo.read()
# print(texto.split("\n"))
# def mSplit(txt:str):
#     return txt.split(",")
# mapeado = list(map(mSplit, texto.split("\n")))
# print(mapeado)

# for i in range(1,10):
#     print(i, end=",")
# n=4
# A = [[0]*n for i in range(n)]
# print(A)
# print(A[1,2])
# for i in range(10,0,-1):
#     print("se jecuta for")

inf = float('inf')
if 100000000000 < inf:
    print("100000000000 < inf")

