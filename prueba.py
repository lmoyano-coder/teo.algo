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

# inf = float('inf')
# if 100000000000 < inf:
#     print("100000000000 < inf")

# out = 'out'
# ha = 'ha'+out
# print(ha)
# x=["o"]
# print(x.append("h"))

# grafo = [[1],[2],[3]]
# e = grafo[1]
# e[0] = 1000
# print(grafo)

# class ListNode():
#     def __init__(self, val:int=0, next=None):
#         self.val = val
#         self.next = next
# def getVal(lista: ListNode | None):
#     if lista == None:
#         return 0
#     return lista.val
# def getNext(lista: ListNode | None):
#     if lista == None:
#         return None
#     return lista.next
# def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
#     resultado = ListNode()
#     inicio = resultado
#     resto = 0
#     while resultado != None:
#         valor = getVal(l1) + getVal(l2) + resto
#         resto = valor >= 10
#         valor -= resto * 10
#         resultado.val = valor # type: ignore
#         l1 = getNext(l1)
#         l2 = getNext(l2)
#         if l1!=None or l2!=None or resto!=0:
#             resultado.next = ListNode() # type: ignore
#         else:
#             resultado.next = None
#         resultado = getNext(resultado)
#     return inicio

# l1= ListNode(2,ListNode(4,ListNode(3)))
# l2= ListNode(5,ListNode(6,ListNode(4)))
# def print_linked_list(list:ListNode | None):
#     if list == None:
#         return
#     if list.next != None:
#         print(list.val,end=" ")
#         print_linked_list(list.next)
#     else:
#         print(list.val)
# print_linked_list(l1)
# print_linked_list(l2)
# result = addTwoNumbers(l1,l2)
# print_linked_list(result)

# prueba_2_l1=ListNode()
# prueba_2_l2=ListNode(7,ListNode(3))
# print_linked_list(prueba_2_l1)
# print_linked_list(prueba_2_l2)
# result = addTwoNumbers(prueba_2_l1,prueba_2_l2)
# print_linked_list(result)

#   sol1, dict
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLength = 0
#         length = len(s)
#         for i in range(length):
#             chosen = {}
#             for j in range(i, length):
#                 if chosen.get(s[j])==None:
#                     chosen[s[j]] = 1
#                 else: break
#             maxLength = max(maxLength, len(chosen))
#         return maxLength
# sol 2, strings
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLength = 0
#         length = len(s)
#         for i in range(length):
#             for j in range(i, length):
#                 if s[j] not in s[i:j]:
#                     maxLength = max(maxLength, len(s[i:j+1]))
#                 else: break
#         return maxLength

# s = "asfasdf"
# print(s[0:0],s[0:1])

# a=[1,2]
# b=[3,2]
# print(max(b[0:1],a[0:0])[0])

# def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
#     l1 = len(nums1)
#     l2 = len(nums2)
#     left1, right1 = 0, l1-1
#     left2, right2 = 0, l2-1
#     length = l1 + l2
#     while right1-left1 + right2-left2 > 1:
#         h1 = (left1 + right1)//2
#         h2 = (left2 + right2)//2
#         if nums1[h1] >= nums2[h2]:
#             if h1+h2+1 > length:
#                 right1 = h1
#             if l1-h1+l2-h2+1 > length:
#                 left2 = h2
#         else: 
#             if len(nums1[0:h1+1])+len(nums2[0:h2]) > length:
#                 right2 = h2
#             if len(nums1[h1+1:l1])+len(nums2[h2:l2]) > length:
#                 left1 = h1
#     return max(nums1[left1:right1],nums2[left2:right2])[0]

# l1,l2=[1,3],[2]
# print(findMedianSortedArrays(l1,l2))

print(range(10))