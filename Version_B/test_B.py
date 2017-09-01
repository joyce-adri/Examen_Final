# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
	# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
	# Reemplazar EL ID por el numero correspondiente del caso de prueba

	def test_tema1_prueba_1(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(120,50001)
		self.assertEqual(p,"Tipo de premio: mini nevera electrolux")

	def test_tema1_prueba_2(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(120,20001)
		self.assertEqual(p,"Tipo de premio: aspiradora electrolux")

	def test_tema1_prueba_3(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(120,10001)
		self.assertEqual(p,"Tipo de premio: arrocera electrolux")

	def test_tema1_prueba_4(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(180,50001)
		self.assertEqual(p,"Tipo de premio: minicomponente LG")

	def test_tema1_prueba_5(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(180,20001)
		self.assertEqual(p,"Tipo de premio: samsumg galaxy J1")

	def test_tema1_prueba_6(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(180,10001)
		self.assertEqual(p,"Tipo de premio: licuadora electrolux")

	def test_tema1_prueba_7(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(360,50001)
		self.assertEqual(p,"Tipo de premio: tv led LG")

	def test_tema1_prueba_8(self):
		p=tema1.premio_por_deposito_a_plazo_fijo(360,20001)
		self.assertEqual(p,"Tipo de premio: tablet samsumg")

	def test_tema1_prueba_9(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(360,10001)
		self.assertEqual(p,"Tipo de premio: microondas electrolux")

		
if __name__ == '__main__':
	unittest.main()