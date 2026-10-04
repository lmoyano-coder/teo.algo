# 5. A raíz de una nueva regulación industrial un fabricante debe rotular cada lote que
# produce según un valor numérico que lo caracteriza. Cada lote está conformado por “n”
# piezas. A cada una de ellas se le realiza una medición de volumen. La regulación considera
# que el lote es válido si más de la mitad de las piezas tienen el mismo volumen. En ese caso el
# rótulo deberá ser ese valor. De lo contrario el lote se descarta. Actualmente cuenta con el
# proceso “A” que consiste en para cada pieza del lote contar cuántas de las restantes tienen el
# mismo volumen. Si alguna de las piezas corresponde al “elemento mayoritario”, lo rotula. De
# lo contrario lo rechaza. Un consultor informático impulsa una solución (proceso “B”) que
# considera la más eficiente: ordenar las piezas por volumen y con ello luego reducir el tiempo
# de búsqueda del elemento mayoritario. Nos contratan para construir una solución mejor
# (proceso “C”). Se pide:
# a. Exprese mediante pseudocódigo el proceso “A”.
# b. Explique si la sugerencia del consultor (proceso “B”) realmente puede mejorar el
# proceso. En caso afirmativo, arme el pseudocódigo que lo ilustre.
# c. Proponga el proceso “C” como un algoritmo superador m
# A: t(n) = t(n-1) + O(n) -> O(n^2) en el peor caso
# B: (supongo busqueda binaria) t(n) = t(n/2) + O(1)->O(logn), pero tarda O(nlogn) en ordenar el lote
# B mejora la solución A
# C: armar un diccionario y usar el volumen como clave, sumando al valor.
# C: t(n) = t(n-1) + O(1) -> O(n) para armar el diccionario + O(n) para elegir el mayor valor
# pero necesito O(n) espacio