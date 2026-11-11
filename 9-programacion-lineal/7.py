# 7. Un estudio de efectos especiales cuenta con una supercomputadora para realizar tareas
# a demanda. Requieren programar en las próximas 40hs dos tipos de tareas:
# “Texturización” de escenas o “iluminación” de escenas. Estas tareas se realizan por
# fotograma. Los pedidos actuales corresponden a 6.000 fotogramas de texturización y
# 4.000 de iluminación. Se conoce que utilizando los programas adecuados se pueden
# realizar 200 y 140 fotogramas por horas por cada tarea respectivamente. Además la
# ganancia por fotograma es de $25 y $30 respectivamente. Debemos decidir mediante
# programación lineal cuantos fotogramas de cada tarea conviene aceptar para maximizar
# la ganancia. Plantee el problema y resuelva gráficamente.

# si la restriccion superior es de 6k y 4k fotogramas:
# max z = x1*25 + x2*30.
# 6000>=x1>=0
# 4000>=x2>=0
# x1/200 + x2/140 <= 40
# en desmos:
# 25x+30y=z
# y>0\left\{6000\ge x\ge0\right\}\left\{4000\ge y\ge0\right\}\left\{\frac{x}{200}+\frac{y}{140}\le40\right\}
# x1 = 6000, x2 = 1400

# si no hay tal restricción
# max z = x1*25 + x2*30.
# x1>=0
# x2>=0
# x1/200 + x2/140 <= 40
# en desmos:
# 25x+30y=z
# y>0\left\{x\ge0\right\}\left\{y\ge0\right\}\left\{\frac{x}{200}+\frac{y}{140}\le40\right\}
# x1 = 8000, x2 = 0