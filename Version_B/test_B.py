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
		p=tema1.premio_por_deposito_a_plazo_fijo(360,55000)
		self.assertEqual(p,"Tipo de premio: tv led LG")

	def test_tema1_prueba_8(self):
		p=tema1.premio_por_deposito_a_plazo_fijo(360,22000)
		self.assertEqual(p,"Tipo de premio: tablet samsumg")

	def test_tema1_prueba_9(self):
		# inserte su codigo de prueba
		p=tema1.premio_por_deposito_a_plazo_fijo(360,11000)
		self.assertEqual(p,"Tipo de premio: microondas electrolux")

	def test_tema2_prueba_1(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(20000, "AAA")
		self.assertEqual(tt,"Tipo de tarjeta: Gold")

	def test_tema2_prueba_2(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(19000, "AAA")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_3(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(15000, "AA")
		self.assertEqual(tt,"Tipo de tarjeta: Platinum")

	def test_tema2_prueba_4(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(20000, "AA")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_5(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(14000, "AA")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_6(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(10000,"A")
		self.assertEqual(tt,"Tipo de tarjeta: Internacional")

	def test_tema2_prueba_7(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(15000,"A")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_8(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(9000,"A")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_9(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(5000,"B")
		self.assertEqual(tt,"Tipo de tarjeta: Club Miles")

	def test_tema2_prueba_10(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(10000,"B")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_11(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(4000,"B")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_12(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(3000, "C")
		self.assertEqual(tt,"Tipo de tarjeta: Advantage")

	def test_tema2_prueba_13(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(5000, "C")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_14(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(2000, "C")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_15(self):
		# inserte su codigo de prueba
		tt=tema2.ofrecer_tarjeta_con_chip(1000, "X")
		self.assertEqual(tt,"Tipo de tarjeta: Clasica")


if __name__ == '__main__':
	unittest.main()