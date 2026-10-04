# El club de amigos de la república Antillense prepara un ágape en sus instalaciones en la
# que desea invitar a la máxima cantidad de sus “n” socios. Sin embargo por protocolo cada
# persona invitada debe cumplir un requisito: Sólo puede asistir si conoce a al menos otras 4
# personas invitadas. Nos solicita seleccionar el mayor número posible de invitados. Proponga
# una estrategia greedy óptima para resolver el problema
# (persona, conocidos), supongo que las personas se conocen mutuamente
# (a, (b, c)), (b, (a, c, d)), (c,(b,a)), (d,(b))
# criterios greedy:
# 1. agregar a la persona con mas conocidos, agregar a sus conocidos y asi sucesivamente.
# 2. agregar a todos, y eliminar a los que no tienen 4 conocidos invitados. La eliminación se repite
# hasta que no se elimine a nadie (porque la eliminar se pueden eliminar conocidos)
# voy a hacerla la 2.
# complejidad espacial: O(n), se guarda como maximo n invitados.
# complejidad temporal: Cada ciclo de eliminacion reviso los n invitados, 
# cada uno haciendo n comparaciones O(1) de invitados, como maximo tendre n ciclos de eliminación.
# entonces O(n^3) de complejidad temporal
# tal vez se pueda bajar la complejidad de buscar conocidos si guardamos el numero de conocidos
# y cuando sacamos un invitado restamos uno a los que lo conocen. Pero si tiene n conocidos no nos ayuda.
# es optimo, ya que eliminamos solo si no tiene cuatro o mas conocidos