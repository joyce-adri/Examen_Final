# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
	
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

#CASOS PRUEBA TEMA 1
	def test_tema1_prueba_1(self):
		plazo = 120
		montoInversion = 50005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: mini nevera electrolux")

	def test_tema1_prueba_2(self):
		plazo = 120
		montoInversion = 20005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: aspiradora electrolux")

	def test_tema1_prueba_3(self):
		plazo = 120
		montoInversion = 10005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: arrocera electrolux")

	def test_tema1_prueba_4(self):
		plazo = 180
		montoInversion = 50005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: minicomponente LG")

	def test_tema1_prueba_5(self):
		plazo = 180
		montoInversion = 20005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: samsumg galaxy J1")

	def test_tema1_prueba_6(self):
		plazo = 180
		montoInversion = 10005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: licuadora electrolux")

	def test_tema1_prueba_7(self):
		plazo = 360
		montoInversion = 50005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: tv led LG")

	def test_tema1_prueba_8(self):
		plazo = 360
		montoInversion = 20005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: tablet samsumg")

	def test_tema1_prueba_9(self):
		plazo = 360
		montoInversion = 10005
		premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEqual(premio,"Tipo de premio: microondas electrolux")

if __name__ == '__main__':
	unittest.main()