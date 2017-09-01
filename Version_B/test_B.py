# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_ID(self):
        # inserte su codigo de prueba
		plazo=120
		montoInversion=50005
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(msg,"Tipo de premio: mini nevera electrolux")

    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
		montoInversion=20005
		plazo=120
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(msg,"Tipo de premio: aspiradora electrolux")
	
	def test_tema3_prueba_ID(self):
		montoInversion=10005
		plazo=120
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(msg,"Tipo de premio: arrocera electrolux")
	
	def test_tema4_prueba_ID(self):
		montoInversion=50005
		plazo=180
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(msg,"Tipo de premio: minicomponente LG")
	
	def test_tema5_prueba_ID(self):
		montoInversion=20005
		plazo=180
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(msg,"Tipo de premio: samsumg galaxy J1")
	
	def test_tema6_prueba_ID(self):
		montoInversion=10005
		plazo=180
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
        self.assertEquals(msg,"Tipo de premio: licuadora electrolux")
	
	def test_tema7_prueba_ID(self):
		montoInversion=50005
		plazo=360
		msg=premio_por_deposito_a_plazo_fijo(plazo,montoInversion)
		self.assertEquals(msg,"Tipo de premio: tv led LG")
	
	def test_tema8_prueba_ID(self):
		montoInversion=20005
		plazo=360
		msg=premio_por_deposito_a_plazo_fijo(plazo,montoInversion)
		self.assertEquals(msg,"Tipo de premio: tablet samsumg")
	
	def test_tema9_prueba_ID(self):
		montoInversion=10005
		plazo=360
		msg=premio_por_deposito_a_plazo_fijo(plazo,montoInversion)
		self.assertEquals(msg,"Tipo de premio: microondas electrolux")
if __name__ == '__main__':
    unittest.main()