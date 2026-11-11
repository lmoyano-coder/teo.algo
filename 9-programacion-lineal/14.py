# 14. Formular el problema de la mochila utilizando programación lineal. Considerar que
# contamos con “n” elementos y conocemos su peso y su valor. El elemento puede estar o
# no dentro de la mochila. También conocemos la capacidad de la mochila. Mediante un
# contraejemplo muestra que pueden existir instancias donde no obtengamos una
# solución apropiada.
# n_{i}
# Sean e los elementos. Sean w los pesos. Sean v los valores. Sea C la capacidad
# maximizamos z = \sum_{i=1}^{n}v_{i}*e_{i}
# Para todo e_{i}, 0 <= e_{i} <= 1 # puede ser 0 o 1
# \sum_{i=1}^{n}w_{i}*e_{i} <= C
# Es discreto, por lo que al colocarse en cada posicion hay que dividir en mitades  y ver la mejor.