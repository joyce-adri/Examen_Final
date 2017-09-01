# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2
from tema1 import premio_por_deposito_a_plazo_fijo

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
        # inserte su codigo de prueba
            plazo = 120
            monto = 15000
            msg = premio_por_deposito_a_plazo_fijo(plazo, monto)
            self.assertEquals(msg, "arrocera electrolux")

    def test_tema1_prueba_2(self):
        # inserte su codigo de prueba
            plazo = 180
            monto = 25000
            msg = premio_por_deposito_a_plazo_fijo(plazo, monto)
            self.assertEquals(msg, "licuadora electrolux")

    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
            plazo = 360
            monto = 52000
            msg = premio_por_deposito_a_plazo_fijo(plazo, monto)
            self.assertEquals(msg, "Microondas Electrolux")
    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
            plazo = 120
            monto = 12000
            msg = premio_por_deposito_a_plazo_fijo(plazo, monto)
            self.assertEquals(msg, "aspiradora electrolux")

    def test_tema1_prueba_5(self):
        # inserte su codigo de prueba
            plazo = 180
            monto = 25000
            msg=premio_por_deposito_a_plazo_fijo(plazo, monto)
            self.assertEquals(msg, "samsumg galaxy J1")


    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        plazo = 360
        monto = 52000
        msg =premio_por_deposito_a_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "Tablet Samsung")


    def test_tema1_prueba_7(self):
        # inserte su codigo de prueba
        plazo = 120
        monto = 15000
        msg =premio_por_deposito_a_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "mini nevera electrolux")

    def test_tema1_prueba_8(self):
        # inserte su codigo de prueba
        plazo = 180
        monto = 25000
        msg = premio_por_deposito_a_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "minicomponente LG")

    def test_tema1_prueba_9(self):
        # inserte su codigo de prueba
        plazo = 360
        monto = 52000
        msg = premio_por_deposito_a_plazo_fijo(plazo, monto)
        self.assertEquals(msg, "tv LED 32 LG")

   # def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        #self.assertEquals()

if __name__ == '__main__':
    unittest.main()