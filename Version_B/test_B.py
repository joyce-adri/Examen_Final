# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
	def test_tema1_prueba_1(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(120,60001)
		self.assertEquals(msg,"Tipo de premio: mini nevera electrolux")

	def test_tema1_prueba_2(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(120,30001)
		self.assertEquals(msg,"Tipo de premio: aspiradora electrolux")
	
	def test_tema1_prueba_3(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(120,15001)
		self.assertEquals(msg,"Tipo de premio: arrocera electrolux")
	
	def test_tema1_prueba_4(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(180,60001)
		self.assertEquals(msg,"Tipo de premio: minicomponente LG")
	
	def test_tema1_prueba_5(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(180,30001)
		self.assertEquals(msg,"Tipo de premio: samsumg galaxy J1")
	
	def test_tema1_prueba_6(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(180,15001)
		self.assertEquals(msg,"Tipo de premio: licuadora electrolux")
	
	def test_tema1_prueba_7(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(360,65001)
		self.assertEquals(msg,"Tipo de premio: tv led LG")
	
	def test_tema1_prueba_8(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(360,35001)
		self.assertEquals(msg,"Tipo de premio: tablet samsumg")
	
	def test_tema1_prueba_9(self):
		msg=tema1.premio_por_deposito_a_plazo_fijo(360,15001)
		self.assertEquals(msg,"Tipo de premio: microondas electrolux")
	
	def test_tema1_prueba_10(self):
			msg=tema1.premio_por_deposito_a_plazo_fijo(460,15001)
			self.assertEquals(msg,"Tipo de premio: no recibe premio")	
		
if __name__ == '__main__':
    unittest.main()