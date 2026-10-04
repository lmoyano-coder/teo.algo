# 2. Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los
# primeros ”m” números naturales ordenados en forma creciente (m >= n). En el vector no hay
# números repetidos. Se desea obtener el menor número no incluido. Ejemplo: [1, 2, 3, 4, 5, 8,
# 9, 11, 12, 13, 14, 20, 22]. Solución: 6. Proponer un algoritmo de tipo división y conquista que
# resuelva el problema en tiempo inferior a lineal. Expresar su relación de recurrencia y
# calcular su complejidad temporal. 
# (supongo que el 0 esta entre los naturales)
# tiene que cumplirse que v[n - 1] <= m, o no habra un número no incluido(ya que no se puede repetir)
# si v[n/2] > m/2, esto significa que hay un número no incluido en la primera mitad
# mismo para v[n/4] > m/4, que nos indica que el numero faltante esta en el primer cuarto
# puede haber otro numero faltante en la segunda mitad, pero, solo nos interesa el menor
# entonces haremos una pseudo busqueda binaria, buscando la menor mitad donde falte un numero 
# e.r.: t(n) = t(n/2) + O(1) => t(n) = t(n/4) + O(1) + O(1) => t(n) = t(n/8) + O(1) + O(1) + O(1)
# Nos queda una suma de operaciones O(1), que se repite log en base 2 de n
# complejidad temporal: O(logn)
# complejidad espacial: O(1) solo para guardar el numero que falta 