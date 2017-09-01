# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from tema1 import *
from tema2 import *

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


    def test_tema2_prueba_1(self):
        tarjeta = Tarjeta().obtener("AAA", 30000)
        self.assertEquals(tarjeta, "gold")

    def test_tema2_prueba_2(self):
        tarjeta = Tarjeta().obtener("AA", 17000)
        self.assertEquals(tarjeta, "platinum")

    def test_tema2_prueba_3(self):
        tarjeta = Tarjeta().obtener("A", 12000)
        self.assertEquals(tarjeta, "internacional")

    def test_tema2_prueba_4(self):
        tarjeta = Tarjeta().obtener("B", 8000)
        self.assertEquals(tarjeta, "club miles")

    def test_tema2_prueba_5(self):
        tarjeta = Tarjeta().obtener("C", 3000)
        self.assertEquals(tarjeta, "advantage")

    def test_tema2_prueba_6(self):
        tarjeta = Tarjeta().obtener("AAA", 10000)
        self.assertEquals(tarjeta, "-")

    def test_tema2_prueba_7(self):
        tarjeta = Tarjeta().obtener("AA", 9000)
        self.assertEquals(tarjeta, "-")

    def test_tema2_prueba_8(self):
        tarjeta = Tarjeta().obtener("A", 7000)
        self.assertEquals(tarjeta, "-")

    def test_tema2_prueba_9(self):
        tarjeta = Tarjeta().obtener("B", 2000)
        self.assertEquals(tarjeta, "-")

    def test_tema2_prueba_10(self):
        tarjeta = Tarjeta().obtener("C", 1000)
        self.assertEquals(tarjeta, "-")

    def test_tema2_prueba_11(self):
        tarjeta = Tarjeta().obtener("D", 100)
        self.assertEquals(tarjeta, "-")


if __name__ == '__main__':
    unittest.main()