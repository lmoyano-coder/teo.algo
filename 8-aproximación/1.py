# Un río posee un conjunto de buques transportadores, cada uno con una capacidad de K kilos que cruzan
#  automóviles de una orilla a la otra. Es un paso muy concurrido y requiere reservar con algunas 
# horas de anticipación para el cruce. En ese proceso los vehículos son registrados y pesados.
# El encargado va cargando los vehículos a medida que se van presentando. En simultáneo va 
# calculando el peso transportado. En el momento que llega un vehículo que de ingresar
#  supere la máxima capacidad de carga. Lo hace esperar. Cierra el barco. El barco cruza, 
# descarga y vuelve por el próximo cargamento.
# a) Demostrarle al encargado que su método puede no utilizar la menor cantidad de viajes posibles.
# b) Demostrarle al encargado que su método no superará el doble de la menor cantidad de 
# viajes posibles para ningún conjunto posible de vehículos y diferentes valores de k

# a) capacidad 1: llega 1/2, lo subo. llega 2/3, no entra, el barco zarpa y vuelve. meto el 2/3.
# llega 1/2, no entra, zarpa el barco y al regresar subo al 1/2. como es el último barco subo y zarpo