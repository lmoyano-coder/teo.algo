# 4. Para determinar si un número es primo existen varios algoritmos propuestos. Entre ellos
# el test de Fermat. Este es un algoritmo randomizado que opera de la siguiente manera: Dado
# un número entero “n”, seleccionar de forma aleatoria un número entero “a” coprimo a n.
# Calcular an-1 módulo n. Si el resultado es diferente a 1, entonces el número “n” es
# compuesto. La parte central de esta operatoria es la potenciación. Podríamos
# algorítmicamente realizarla de la siguiente manera:
# pot = 1
# Desde i=1 a n-1
# pot = pot * a
# En este caso se realizan o(n) multiplicaciones. Proponga un método usando división y
# conquista que resuelva la potenciación con menor complejidad temporal.
# al guardar el resultado, me ahorra mult
# 2^2: 2*2 -> O(1) vs 2*2 -> O(1)
# 2^3: a=2*2, a*2 -> O(2) vs 2*2*2 -> O(2)
# 2^4: a=2*2, a*a -> O(2) vs 2*2*2*2 -> O(3)
# es decir descompongo la potencia:
# 7 -> 6 + 1 -> 3 + 3 + 1 -> O(2) + O(1)(para multiplicar los 3) + O(1) -> O(4)
# 13 -> 12 + 1 -> 6 + 6 + 1 -> O(3) + O(1)(para multiplicar los 6) + O(1) -> O(5) vs O(12)
# entonces la cant de mult para un n será la cant de mult de n/2 + 2 (como maximo)
# hay 2 casoss para la ecuaciond e recurrencia:
# n par: t(n) = t(n/2) + O(1) -> una llamada recursiva y otra para mult. el resultado 
# n impar: t(n) = t(n/2) + O(2) -> t(n) = t(n/4) + O(1) + O(2)(pq el proximo caso de un impar sera par)
# en el peor de los casos realizare una alternaciond entre O(1) y O(2) tomo promedio->O(1.5)
# la cantidad de operaciones realizadas será una suma de O(1.5) hasta llegar al caso base 2 o 3
# o sea: se repetira como mucho logn veces
# entonces: complejidad temporal O(1.5logn)->O(logn)
# espacial: estoy guardando como mucho 2 numeros(resultado, result^2)-> O(1) 