# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=120, montoInversion=50002)
        self.assertEquals(premio, "Tipo de premio: mini nevera electrolux")

    def test_tema1_prueba_2(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=120, montoInversion=20002)
        self.assertEquals(premio, "Tipo de premio: aspiradora electrolux")

    def test_tema1_prueba_3(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=120, montoInversion=10002)
        self.assertEquals(premio, "Tipo de premio: arrocera electrolux")

    def test_tema1_prueba_4(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=180, montoInversion=50002)
    	self.assertEquals(premio, "Tipo de premio: minicomponente LG")

    def test_tema1_prueba_5(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=180, montoInversion=20002)
    	self.assertEquals(premio, "Tipo de premio: samsumg galaxy J1")

    def test_tema1_prueba_6(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=180, montoInversion=10002)
    	self.assertEquals(premio, "Tipo de premio: licuadora electrolux")

    def test_tema1_prueba_7(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=360, montoInversion=50002)
    	self.assertEquals(premio, "Tipo de premio: tv led LG")

    def test_tema1_prueba_8(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=360, montoInversion=20002)
    	self.assertEquals(premio, "Tipo de premio: tablet samsumg")

    def test_tema1_prueba_9(self):
    	premio = premio_por_deposito_a_plazo_fijo(plazo=360, montoInversion=10002)
    	self.assertEquals(premio, "Tipo de premio: microondas electrolux")







    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()