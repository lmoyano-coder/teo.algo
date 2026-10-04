# 15. Dentro de un país existen dos colonias subacuáticas cada una de ellas con “n”
# habitantes. Cada habitante tiene su documento de identidad único identificado por un
# número. Para una tarea especial se decidió seleccionar a aquella persona que vive en alguna
# de las colonias cuyo número de documento corresponda a la mediana de todos los números
# de documento presentes en ellas. Por una cuestión de protocolo no nos quieren dar los
# listados completos de documentos. Solo nos responden de cada colonia ante la consulta
# “Cual es el documento en la posición X de todos los habitantes de la isla ordenados de mayor
# a menor”. Utilizando esto, proponer un algoritmo utilizando división y conquista que
# resuelva el problema 
# solucion naive: pido todas las posiciones y reconstruyo la menor. O(n)
# isla u e isla v
# otro algo: obtengo a=u[n/2]. Sea 'x' la pos de a en u e 'y' la pos de a en v.(las pos van de 1 a n)
# si x + y = n + 1 -> a = el mediano (hay que buscar a su vecino total con bb)
# si x + y > n + 1 -> a = el medio de la mitad menor, y actualizo x e y.
# si x + y < n + 1 -> a = el medio de la mitad mayor, y actualizo x e y.
# si se agotaron todos los números de u, hago el mismo proceso en v
# así recursiva mente hasta llegar al caso 1
# si se agotaron todos los números de u, hago el mismo proceso en v
# como 2n es par, la mediana es el promedio entre los dos numeros que esten en el medio
# como ya obtuve uno, solo hace falta buscar su vecino, otra busqueda binaria
# si n es par (no hay mediana), seleccionar el que queda a la izquierda del medio
# t(n) = t(n/2) + O(logn) ->busco la ubicacion de a en v mediante busqueda binaria
# si es el mediano; busco su vecino y devuelo el promedio.
# si no es: Llamo a la funcion en alguna de las mitades
# complejidad -> O((logn)*(logn))
# 1:(1,3,8,12,13,15,20,36,39)
# 2:(2,4,5,6,7,9,10,25,58)
# total: (1,2,3,4,5,6,7,8,9,10,12,13,15,20,25,36,39,58)
# u:(1,3,6)
# v:(2,4,5) #mediano es 3.5
# u:(1,9,11)
# v:(2,4,5)
# u:(1,5,8,11)
# v:(2,3,4,6)


