# 4. El problema de bin packing es un problema de optimización que busca ubicar un
# conjunto de elementos E dentro de la menor cantidad posible de contenedores. Cada
# elemento “i” tiene un peso wi
# . Los contenedores son ilimitados, idénticos y pueden
# soportar P peso. Proponer resolver este problema utilizando algoritmos genéticos.

# individuo: vector de enteros. pueden tomar desde 0 hasta E-1. cada pos representa un elemento
# generación: al inicio de la generacion se chequea que todos los individuos respeten que en cada 
# contenedor solo haya <=p peso.
# Los individuos de una generacion, excepto la primera, son producto del cruce de dos elite anteriores
# los elite son los individuos en el 50% con mejor solucion. Cada posicion del gen del hijo tiene
# 1/2 chance de ser de su padre1 y 1/2 de padre2. Luego de ser seleccionado, cada pos tiene 1/e chance
# de ser mutado por un numero aleatorio del rango [0,e-1]. Cada pareja tendra 4 hijos.
# repito hasta la cantidad de iteraciones que se quiere o a la precisión de la solucion que se quiera