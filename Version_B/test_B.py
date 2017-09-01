# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from tema1 import *
import tema1
import tema2


class Test(unittest.TestCase):

# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema1_prueba_1(self):
        plazo = 120
        monto = 15000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Arrocera Electrolux 1.8L")

    def test_tema1_prueba_2(self):
        plazo = 120
        monto = 28000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Aspiradora Electrolux")

    def test_tema1_prueba_3(self):
        plazo = 120
        monto = 55000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Mini nevera 5 pies Electrolux")

    def test_tema1_prueba_4(self):
        plazo = 180
        monto = 16000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo,monto)
        self.assertEquals(msg,"Licuadora 5 velocidades Electrolux")

    def test_tema1_prueba_5(self):
        plazo = 180
        monto = 35000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Samsung Galaxy J1")

    def test_tema1_prueba_6(self):
        plazo = 180
        monto = 60000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Minicomponente LG")

    def test_tema1_prueba_7(self):
        plazo = 360
        monto = 12000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Microondas Electrolux 20L")

    def test_tema1_prueba_8(self):
        plazo = 360
        monto = 40000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Tablet Samsung")

    def test_tema1_prueba_9(self):
        plazo = 360
        monto = 70000
        premios = Banco()
        msg = premios.premios_depositos_plazo_fijo(plazo, monto)
        self.assertEquals(msg,"Tv LED 32 LG")

    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()
