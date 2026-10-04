from flujoMaximo import *
def prueba_aumentar_camino():
    #      s, 1, 2,3,4,t
    g = [[-20,20,0,0,0,0],[-10,0,10,0,0,0],[0,-30,0,30,0,0],
            [0,0,-10,10,0,0],[0,-10,0,0,10,0],[0,0,0,0,-20,20],
            [0,0,0,-20,0,20],[0,20,0,-20,0,0]]
    f = [20,0,20,0,0,0,20]
    print("gr previo al aumentar camino",(construir_gr(g,f)))
    s,t = 0, len(g[0])-1
    e_s_1=0
    e_s_2=1
    e_1_3=2
    e_2_3=3
    e_1_4=4
    e_4_5=5
    e_3_5=6
    e_3_1=7
    print(f)
    aumentar_flujo_camino([e_s_2,e_2_3,e_3_1,e_1_4,e_4_5], f, g)
    print(f)
def prueba_crear_gr():
    #      s, 1, 2,3,4,t
    g = [[-20,20,0,0,0,0],[-10,0,10,0,0,0],[0,-30,0,30,0,0],
            [0,0,-10,10,0,0],[0,-10,0,0,10,0],[0,0,0,0,-20,20],
            [0,0,0,-20,0,20]]
    f = [20,0,20,0,0,0,20]
    gr = construir_gr(g,f)
    print("gr previo al aumentar camino\n", gr)
    s,t = 0, len(g[0])-1
    e_s_1=0
    e_s_2=1
    e_1_3=2
    e_2_3=3
    e_1_4=4
    e_4_5=5
    e_3_5=6
    e_3_1=7
    print(f)
    aumentar_flujo_camino([e_s_2,e_2_3,e_3_1,e_1_4,e_4_5], f, gr)
    print(f)
def prueba_proximo_camino():
    #      s, 1, 2,3,4,t
    g = [[-20,20,0,0,0,0],[-10,0,10,0,0,0],[0,-30,0,30,0,0],
            [0,0,-10,10,0,0],[0,-10,0,0,10,0],[0,0,0,0,-20,20],
            [0,0,0,-20,0,20]]
    f = [20,0,20,0,0,0,20]
    gr = construir_gr(g,f)
    print("gr previo al aumentar camino\n", gr)
    print("proximo camino:\n",proximo_camino(gr,f))
def prueba_flujo_maximo():
    #      s, 1, 2,3,4,t
    g = [[-20,20,0,0,0,0],[-10,0,10,0,0,0],[0,-30,0,30,0,0],
            [0,0,-10,10,0,0],[0,-10,0,0,10,0],[0,0,0,0,-20,20],
            [0,0,0,-20,0,20]]
    f = [0,0,0,0,0,0,0]
    print("g:\n", g)
    print("f antes de flujo maximo:\n", f)
    print(flujo_maximo(g,f))
    print("f despues de flujo maximo:\n", f)
# prueba_aumentar_camino()
# prueba_crear_gr()
# prueba_proximo_camino()
prueba_flujo_maximo()