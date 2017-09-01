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

	
if __name__ == '__main__':
	unittest.main()