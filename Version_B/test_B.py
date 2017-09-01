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

	# def test_tema1_prueba_7(self):
	# 	plazo = 360
	# 	montoInversion = 50005
	# 	premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
	# 	self.assertEqual(premio,"Tipo de premio: tv led LG")

	# def test_tema1_prueba_8(self):
	# 	plazo = 360
	# 	montoInversion = 20005
	# 	premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
	# 	self.assertEqual(premio,"Tipo de premio: tablet samsumg")

	# def test_tema1_prueba_9(self):
	# 	plazo = 360
	# 	montoInversion = 10005
	# 	premio = tema1.premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
	# 	self.assertEqual(premio,"Tipo de premio: microondas electrolux")

#CASOS PRUEBA TEMA 2
	def test_tema2_prueba_1(self):
		tipoCliente = 'AAA'
		montoDeuda = 20000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Gold")

	def test_tema2_prueba_2(self):
		tipoCliente = 'AAA'
		montoDeuda = 19999
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_3(self):
		tipoCliente = 'AA'
		montoDeuda = 14999
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_4(self):
		tipoCliente = 'AA'
		montoDeuda = 20000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_5(self):
		tipoCliente = 'AA'
		montoDeuda = 15000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Platinum")

	def test_tema2_prueba_6(self):
		tipoCliente = 'A'
		montoDeuda = 9999
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_7(self):
		tipoCliente = 'A'
		montoDeuda = 15000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_8(self):
		tipoCliente = 'A'
		montoDeuda = 10000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Internacional")

	def test_tema2_prueba_9(self):
		tipoCliente = 'B'
		montoDeuda = 4999
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_10(self):
		tipoCliente = 'B'
		montoDeuda = 10000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_11(self):
		tipoCliente = 'B'
		montoDeuda = 5000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Club Miles")

	def test_tema2_prueba_12(self):
		tipoCliente = 'C'
		montoDeuda = 2999
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_13(self):
		tipoCliente = 'C'
		montoDeuda = 5000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

	def test_tema2_prueba_14(self):
		tipoCliente = 'C'
		montoDeuda = 3000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Advantage")

	def test_tema2_prueba_15(self):
		tipoCliente = 'F'
		montoDeuda = 1000
		tarjeta = tema2.ofrecer_tarjeta_con_chip(montoDeuda, tipoCliente)
		self.assertEqual(tarjeta,"Tipo de tarjeta: Clasica")

if __name__ == '__main__':
	unittest.main()