import unittest

from grafoSonic import *

class TestFestivalGrafo(unittest.TestCase):
    def assertAristaIgual(self,aristaEsperada, aristaDudosa):
        for i in range(len(aristaEsperada)):
            self.assertEqual(aristaEsperada[i], aristaDudosa[i])
    def assertGrafoIgual(self, grafoEsperado, grafoDudoso):
        for e in range(len(grafoEsperado)):
            self.assertAristaIgual(grafoEsperado[e],grafoDudoso[e])
    def test_01crearGrafoDeVacioDevuelveVacio(self):
        grafo = crear_grafo([],[],[],[],[])
        self.assertTrue(grafo==[])
    def test_02crearGrafoDe1banda1servidor1plataformaDevuelveUnaRecta(self):
        bandas = [('b1',1)]
        servidores = [('j1',1)]
        plataformas = [('p1',1)]
        bs = [('b1','j1')]
        sp = [('j1','p1')]
        esperado = [['fuente','b1',1],['b1','j1',1],['j1','j1out',1],['j1out','p1',1],['p1','sumidero',1]]
        
        respuesta = crear_grafo(bandas, servidores, plataformas, bs, sp)

        self.assertEqual(len(respuesta), len(esperado))
        self.assertGrafoIgual(esperado, respuesta)
    def test_03crearGrafoCon2bandas1servidorY2Plataformas(self):
        bandas = [('b1',1),('b2',1)]
        servidores = [('j1',2)]
        plataformas = [('p1',1),('p2',1)]
        bs = [('b1','j1'),('b2','j1')]
        sp = [('j1','p1'),('j1','p2')]
        esperado = [['fuente','b1',1],['fuente','b2',1],['b1','j1',1],['b2','j1',1],['j1','j1out',2],['j1out','p1',2],
                    ['p1','sumidero',1],['j1out','p2',2],['p2','sumidero',1]]
        
        respuesta = crear_grafo(bandas, servidores, plataformas, bs, sp)

        self.assertEqual(len(respuesta), len(esperado))
        self.assertGrafoIgual(esperado, respuesta)

class TestFestivasFlujoMax(unittest.TestCase):
    def assertAristaIgual(self,aristaEsperada, aristaDudosa):
        for i in range(len(aristaEsperada)):
            self.assertEqual(aristaEsperada[i], aristaDudosa[i])
    def assertGrafoIgual(self, grafoEsperado, grafoDudoso):
        for e in range(len(grafoEsperado)):
            self.assertAristaIgual(grafoEsperado[e],grafoDudoso[e])
    def test_01construirGrConFNuloDevuelveLoMismo(self):
        esperado = [['fuente','b1',1],['fuente','b2',1],['b1','j1',1],['b2','j1',1],['j1','j1out',2],['j1out','p1',2],
                    ['p1','sumidero',1],['j1out','p2',2],['p2','sumidero',1]]
        respuesta = construir_gr(esperado, [0]*len(esperado))
        self.assertGrafoIgual(esperado, respuesta)
    def test_02construirGrconVacioDevuelveVacio(self):
            respuesta = construir_gr([], [])
            esperado = []
            self.assertGrafoIgual(esperado, respuesta)
    def test_03(self):
        g = [['fuente','b1',1],['b1','j1',1],['j1','j1out',1],['j1out','p1',1],['p1','sumidero',1]]
        f = [1,1,1,1,1]
        respuesta = construir_gr(g,f)
        esperado = g.copy()
        esperado.append(['b1','fuente',1])
        esperado.append(['j1','b1',1])
        esperado.append(['j1out','j1',1])
        esperado.append(['p1','j1out',1])
        esperado.append(['sumidero','p1',1])
        self.assertEqual(len(esperado), len(respuesta))
        self.assertGrafoIgual(esperado, respuesta)
    def test_04esAdelante4deFdeLargo4DevuelveFalse(self):
        f = [0]*4
        e = 4
        self.assertFalse(es_adelante(e,f))
    def test_05esAdelante1deFdeLargo3DevuelveTrue(self):
            f = [0]*3
            e = 1
            self.assertTrue(es_adelante(e,f))
    def test_06flujoMaximoDe3NodosConCapacidad1esFconTodosUnos(self):
        g = [['fuente','nodo1',1],['nodo1','sumidero',1]]
        f = ford_fulkerson_dinic(g)
        self.assertEqual(f[0],1)
        self.assertEqual(f[1],1)
    def test_07flujoMaximoResultadoCorrecto(self):
            g = [['fuente','2',10],['fuente','1',20],['2','3',10],['1','3',30],
                    ['1','4',10],['3','sumidero',20],['4','sumidero',10]]
            f = ford_fulkerson_dinic(g)
            self.assertEqual(f[0],10)
            self.assertEqual(f[1],20)
            self.assertEqual(f[2],10)
            self.assertEqual(f[3],10)
            self.assertEqual(f[4],10)
            self.assertEqual(f[5],20)
            self.assertEqual(f[6],10)
    def test08ejercicioDeLaCatedra(self):
        bandas = [('KUNAI',7),('VÖLSA',5),('TREMOR',6)]
        servidores = [('ZARZA',8),('MIRLO',7),('OTEO',5)]
        plataformas = [('ONDA',10),('CRISOL',8)]
        banda_servidor = [('KUNAI','ZARZA'),('KUNAI','MIRLO'),('VÖLSA','MIRLO'),
                            ('VÖLSA','OTEO'),('TREMOR','ZARZA'),('TREMOR','OTEO')]
        servidor_plataforma = [('ZARZA','ONDA'),('MIRLO','ONDA'),('MIRLO','CRISOL'),
                            ('OTEO','CRISOL')]
        posible, Max, asignacion = 0, 1, 2
        asignacionEsperada = [['KUNAI', 'ONDA', 4], ['KUNAI', 'CRISOL', 3], 
                            ['VÖLSA', 'CRISOL', 5], ['TREMOR', 'ONDA', 6]]
        flujoMax = 18
        resultado = main(bandas, servidores, plataformas,banda_servidor,servidor_plataforma)
        self.assertTrue(resultado[posible])
        self.assertEqual(flujoMax,resultado[Max])
        self.assertGrafoIgual(asignacionEsperada, resultado[asignacion])
    def test_09ejemplo_del_enunciado_factible(self):
        bandas = [("B1", 6), ("B2", 4)]
        servidores = [("S1", 5), ("S2", 6)]
        plataformas = [("P1", 5), ("P2", 5)]
        bs = [("B1", "S1"), ("B1", "S2"), ("B2", "S2")]
        sp = [("S1", "P1"), ("S2", "P1"), ("S2", "P2")]
        asignacionEsperada = [['B1', 'P1', 5], ['B1', 'P2', 1], ['B2', 'P2', 4]]
        posible, flujo_max, asignacion = main(bandas, servidores, plataformas, bs, sp)
        self.assertTrue(posible)
        self.assertEqual(flujo_max, 10)
        self.assertGrafoIgual(asignacionEsperada, asignacion)
    def test_10cambiarCapaciadUnoMenos(self):
        bandas = [("B1", 6), ("B2", 4)]
        servidores = [("S1", 5), ("S2", 6)]
        plataformas = [("P1", 5), ("P2", 5)]
        bs = [("B1", "S1"), ("B1", "S2"), ("B2", "S2")]
        sp = [("S1", "P1"), ("S2", "P1"), ("S2", "P2")]
        asignacionEsperada = [['B1', 'P1', 5], ['B2', 'P2', 4]]
        flujoMaxEsperado = 9
        main(bandas, servidores, plataformas, bs, sp)
        posible, flujoMax, asignacion = actualizar_servidor("S2",4)
        self.assertFalse(posible)
        self.assertEqual(flujoMax, flujoMaxEsperado)
        self.assertGrafoIgual(asignacionEsperada, asignacion)
    def test_11cambiarCapacdadA0(self):
        bandas = [("B1", 6), ("B2", 4)]
        servidores = [("S1", 5), ("S2", 6)]
        plataformas = [("P1", 5), ("P2", 5)]
        bs = [("B1", "S1"), ("B1", "S2"), ("B2", "S2")]
        sp = [("S1", "P1"), ("S2", "P1"), ("S2", "P2")]
        asignacionEsperada = [['B1', 'P1', 5]]
        flujoMaxEsperado = 5
        main(bandas, servidores, plataformas, bs, sp)
        posible, flujoMax, asignacion = actualizar_servidor("S2",0)
        self.assertFalse(posible)
        self.assertEqual(flujoMax, flujoMaxEsperado)
        self.assertGrafoIgual(asignacionEsperada, asignacion)
if __name__ == "__main__":
    unittest.main()