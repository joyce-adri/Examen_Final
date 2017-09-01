# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema1_prueba_1(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(120, 15000)
        self.assertEquals(premio, "arrocera electrolux 1.8l")

    def test_tema1_prueba_2(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(120 , 25000)
        self.assertEquals(premio, "aspiradora electrolux")

    def test_tema1_prueba_3(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(120, 100000)
        self.assertEquals(premio, "mini nevera 5 pies electrolux")

    def test_tema1_prueba_4(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(180, 15000)
        self.assertEquals(premio, "licuadora 5 velocidades electrolux")

    def test_tema1_prueba_5(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(180, 25000)
        self.assertEquals(premio, "samsung galaxy j1")

    def test_tema1_prueba_6(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(180, 100000)
        self.assertEquals(premio, "minicomponente lg")

    def test_tema1_prueba_7(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(360, 15000)
        self.assertEquals(premio, "microondas electrolux 20l")

    def test_tema1_prueba_8(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(360, 25000)
        self.assertEquals(premio, "tablet samsung")

    def test_tema1_prueba_9(self):
        premio = PremiosDepositosPlazoFijo().obtenerPremio(360, 100000)
        self.assertEquals(premio, "tv led 32 lg")


    #def test_tema2_prueba_ID(self):
     #   # inserte su codigo de prueba
     #   self.assertEquals()

if __name__ == '__main__':
    unittest.main()