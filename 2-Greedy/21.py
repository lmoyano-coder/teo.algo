# 21. Un servidor de videojuegos se alquila por horas. El contrato dura un tiempo fijo y
# permite utilizar en forma exclusiva el mismo por una cantidad continua de horas una vez por
# semana. Por cada contrato que el dueño del servidor establece, se lleva un monto fijo de
# dinero. Al dueño del servidor le interesa tener la mayor cantidad de contratos posibles (sin
# importar la duración en horas de los mismos). El servidor funciona las 24hs. Recibe un
# conjunto de ofertas de contrato y debe seleccionar cuales aceptar. Cada contrato tiene un
# día y hora de inicio y un día y hora de fin. Durante ese lapso tendrán la exclusividad del
# servidor. Ese tiempo contiguo no puede durar más de 1 semana (un contrato podría pedir
# por ejemplo 3 días completos pero nunca superar la semana).. Y esa fecha se repite todas las
# semanas. Los contratos aceptados no deben superponerse. Proponer una solución greedy
# que solucione el problema de forma óptima. Tenga en cuenta que es posible contratos que
# empiecen al finalizar la semana y terminen horas después del inicio de la misma.
# ((1,3:45),(1,6:00))
# 1. agarrar el mas corto
# 2. agarrar el que tiene menos superposicion
# 3. agarrar el mas corto, y luego el que termine antes.
# 4. agarrar el que tiene menos superposicion, y luego el que termine antes.
# contraejemplo 1: ((1,1:00),(1,5:00)) ((1,4:00),(1,7:00)) ((1,6:00),(1,12:00))
# elije el 2, y el optimo es 1 y 3, aunque duren mas, el 3 es desprovado idem
# 2 y 4 parecen optimos. por Ockham's razor, elije 2
# contraejemplo: el de la filmina de greedy (pag 13)
# nuevo criterior: Selecciono el que termina antes (y haya iniciado esta semana)