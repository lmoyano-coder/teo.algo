# 1. La sala de guardia de un hospital tiene que tener al menos un médico en todos los
# feriados y en los fines de semana largos de feriados. Cada profesional indica sus
# posibilidades: por ejemplo alguien puede estar de guardia en cualquier momento del fin de
# semana largo del 9 de julio (p. ej. disponibilidad de A para el 9 de julio = (Jueves 9/7, Viernes
# 10/7, Sábado 11/7, Domingo 12/7)), también puede suceder que alguien pueda sólo en parte
# (por ejemplo, disponibilidad de B para 9 de julio = (Jueves 9/7, Sábado 11/7, Domingo 12/7)).
# Aunque los profesionales tengan múltiples posibilidades, a cada uno se lo puede convocar
# para un solo día (se puede disponer de B sólo en uno de los tres días que indicó). Para
# ayudar a la sala de guardia a planificar cómo se cubren los feriados durante todo el año
# debemos resolver el problema de las guardias: Existen k períodos de feriados (por ejemplo, 9
# de julio es un período de jueves 9/7 a domingo 12/7, en 2019 Día del Trabajador fue un
# período de 1 día: miércoles 1 de mayo, etc.). Dj es el conjunto de fechas que se incluyen en el
# período de feriado j-ésimo. Todos los días feriados son los que resultan de la unión de todos
# los Dj. Hay n médicos y cada médico i tiene asociado un conjunto Si de días feriados en los
# que puede trabajar (por ejemplo B tiene asociado los días Jueves 9/7, Sábado 11/7, Domingo
# 12/7, entre otros).
# Proponer un algoritmo polinomial (usando flujo en redes) que toma esta información y
# devuelve qué profesional se asigna a cada día feriado (o informa que no es posible resolver
# el problema) sujeto a las restricciones:
# - Ningún profesional trabajará más de F días feriados (F es un dato), y sólo en días en
# los que haya informado su disponibilidad.
# - A ningún profesional se le asignará más de un feriado dentro de cada período Dj.

# Cuando construimos el grafo, tenemos n nodos de S (medicos) y k * n nodos de D (feriadosQuePuedeTrabajar)
# y t nodos de T (dias feriados).
# Cada medico tiene p feriados en los que puede trabajar al menos un día, representados por nodos de D
# Cada nodo de D corresponde a uno de los k feriados, y esta conectado a uno de los t nodos de T
# la capacidad de cada conexión de Si a Di es de 1 (solo puede trabajar un dia de cada feriado)
# la capacidad de cada conexión de Di a Ti será 1 (un trabajador que puede ese feriado trabaja ese dia)
# De cada Ti saldra una conexión a un sumidero que crearemos. Debe recibir t de flujo (dias trabajados)
# De Una fuente que creamos saldra t de flujo hacia los n medicos, con capacidad F en cada conexion
# Aplicamos la funcio de flujoMaximo-FordFulkerson()