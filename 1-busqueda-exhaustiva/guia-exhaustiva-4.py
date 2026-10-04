# 4. En un tablero de ajedrez (una cuadrícula de 8x8) se ubica la pieza llamada “caballo”
# en la esquina superior izquierda. Un caballo tiene una manera peculiar de moverse por el
# tablero: Dos casillas en dirección horizontal o vertical y después una casilla más en
# ángulo recto (formando una forma similar a la letra “L”). El caballo se traslada de la casilla
# inicial a la final sin tocar las intermedias, dado que las “salta”. Se quiere determinar si es
# posible, mover esta pieza de forma sucesiva a través de todas las casillas del tablero,
# pasando una sola vez por cada una de ellas, y terminando en la casilla inicial. Plantear la
# solución mediante backtracking
def sumar_par(par1, par2):
    return [par1[0]+par2[0], par1[1]+par2[1]]
def restar_par(par1, par2):
    return [par1[0]-par2[0], par1[1]-par2[1]]
class tablero:
    casillas:list = [] #lista de listas de 0
    pintadas:list = [] #lista de casillas pintadas
    largo:int
    cant_pintadas:int = 0 #cantidad total pintada (distinta de 0)
    mas_lejos:int = 0
    cant_llamada_pintar:int = 0
    ultimo_print:int = 0
    paso_print:int
    def __init__(self, largo, paso_print):
        self.largo = largo
        self.paso_print = paso_print
        for i in range(largo):
            self.casillas.append([0] * largo)
    def posibles_movimientos(self, posicion):
        t = self.casillas #tablero
        movimientos = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2),(1,-2),(-1,2),(-1,-2)]
        posibles = []
        for i, m in enumerate(movimientos):
            casilla = sumar_par(posicion, m)
            if casilla[0] >= 0 and casilla[0] <= self.largo-1 and casilla[1] >= 0 and casilla[1] <= self.largo-1:
                if not self.esta_pintado(casilla):
                    posibles.append(casilla)
        return posibles
    def esta_pintado(self, casilla):
        # return casilla in self.pintadas
        return self.casillas[casilla[0]][casilla[1]] #0 si no esta pintada, 1 si si
    def despintar(self, casilla):
        # if casilla in self.pintadas:
        #     self.pintadas.remove(casilla)
        #     self.cant_pintadas -= 1
        self.casillas[casilla[0]][casilla[1]] = 0
        self.cant_pintadas -= 1
    def pintar(self, casilla):
        # self.pintadas.append(casilla)
        self.casillas[casilla[0]][casilla[1]] = 1
        self.cant_pintadas += 1
        if self.cant_pintadas > self.mas_lejos:
            self.mas_lejos = self.cant_pintadas
        self.cant_llamada_pintar += 1
        if (self.cant_llamada_pintar > self.ultimo_print + self.paso_print):
            print(self.cant_pintadas, " ", self.mas_lejos, " ", self.cant_llamada_pintar)
            self.ultimo_print = self.cant_llamada_pintar

board = tablero(8,1000000)

def saltar(casilla, inicial):
    if casilla == inicial and board.cant_pintadas >= 64:
        return True
    for c in board.posibles_movimientos(casilla):
        board.pintar(casilla)
        if saltar(c, inicial) == True:
            return True
        board.despintar(casilla)
    return False
def iniciar():
    return saltar([0,0],[0,0])
print(iniciar())
print(board.pintadas)