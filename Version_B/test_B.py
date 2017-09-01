# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
        plazo1 = 120
        montoInversion1 = 50001
        msg = premio_por_deposito_a_plazo_fijo(plazo1, montoInversion1)
        self.assertEquals(msg,"mini nevera electrolux")

    def test_tema1_prueba_2(self):
        plazo2 = 120
        montoInversion2 = 25000
        msg = premio_por_deposito_a_plazo_fijo(plazo2, montoInversion2)
        self.assertEquals(msg,"aspiradora electrolux")
        
    def test_tema1_prueba_3(self):
        plazo3 = 120
        montoInversion3 = 15000
        msg = premio_por_deposito_a_plazo_fijo(plazo3, montoInversion3)
        self.assertEquals(msg,"arrocera electrolux")

    def test_tema1_prueba_4(self):
        plazo4 = 180
        montoInversion4 = 50001
        msg = premio_por_deposito_a_plazo_fijo(plazo4, montoInversion4)
        self.assertEquals(msg,"minicomponente LG")

    def test_tema1_prueba_5(self):
        plazo5 = 180
        montoInversion5 = 25000
        msg = premio_por_deposito_a_plazo_fijo(plazo5, montoInversion5)
        self.assertEquals(msg,"samsumg galaxy J1")

    def test_tema1_prueba_6(self):
        plazo6 = 180
        montoInversion6 = 15000
        msg = premio_por_deposito_a_plazo_fijo(plazo6, montoInversion6)
        self.assertEquals(msg,"licuadora electrolux")

    def test_tema1_prueba_7(self):
        plazo7 = 360
        montoInversion7 = 50001
        msg = premio_por_deposito_a_plazo_fijo(plazo7, montoInversion7)
        self.assertEquals(msg,"tv led LG")

    def test_tema1_prueba_8(self):
        plazo8 = 360
        montoInversion8 = 25000
        msg = premio_por_deposito_a_plazo_fijo(plazo8, montoInversion8)
        self.assertEquals(msg,"tablet samsumg")

    def test_tema1_prueba_9(self):
        plazo9 = 360
        montoInversion9 = 15000
        msg = premio_por_deposito_a_plazo_fijo(plazo9, montoInversion9)
        self.assertEquals(msg,"microondas electrolux")

    def test_tema1_prueba_10(self):
        plazo10 = 120
        montoInversion10 = 9000
        msg = premio_por_deposito_a_plazo_fijo(plazo10, montoInversion10)
        self.assertEquals(msg,"no recibe premio")

        
        

    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()
