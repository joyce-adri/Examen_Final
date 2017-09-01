# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from tema1 import *
from tema2 import *



class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
	def test_tema1_prueba_ID(self):
        #id:1
		plazo=120
		montoInversion=50005
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: mini nevera electrolux")
	def test_tema2_prueba_ID(self):
        #id:2
		montoInversion=20005
		plazo=120
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: aspiradora electrolux")
	def test_tema3_prueba_ID(self):
		#id:3
		montoInversion=10005
		plazo=120
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: arrocera electrolux")
	def test_tema4_prueba_ID(self):
		#id:4
		montoInversion=50005
		plazo=180
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: minicomponente LG")
	def test_tema5_prueba_ID(self):
		#id:5
		montoInversion=20005
		plazo=180
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: samsumg galaxy J1")
	def test_tema6_prueba_ID(self):
		#id:6
		montoInversion=10005
		plazo=180
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: licuadora electrolux")
	def test_tema7_prueba_ID(self):
		#id:7
		plazo=360
		montoInversion=50005
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: tv led LG")
	def test_tema8_prueba_ID(self):
		#id:8
		plazo=360
		montoInversion=20005
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: tablet samsumg")
	def test_tema9_prueba_ID(self):
		#id:9
		plazo=360
		montoInversion=10005
		msg=premio_por_deposito_a_plazo_fijo(plazo, montoInversion)
		self.assertEquals(msg,"Tipo de premio: microondas electrolux")
	def test_tema10_prueba_ID(self):
		#id:10
		msg=premio_por_deposito_a_plazo_fijo(180,10)
		self.assertEquals(msg,"Tipo de premio: no recibe premio")
	def test_tema11_prueba_ID(self):
	#id:11
		msg=ofrecer_tarjeta_con_chip(20005, "AAA")
		self.assertEquals(msg,"Tipo de tarjeta: Gold")
	def test_tema12_prueba_ID(self):
	#id:12
		msg=ofrecer_tarjeta_con_chip(15000, "AA")
		self.assertEquals(msg,"Tipo de tarjeta: Platinum")
	def test_tema13_prueba_ID(self):
	#id:13
		msg=ofrecer_tarjeta_con_chip(10005, "A")
		self.assertEquals(msg,"Tipo de tarjeta: Internacional")
	def test_tema14_prueba_ID(self):
	#id:14
		msg=ofrecer_tarjeta_con_chip(5003, "B")
		self.assertEquals(msg,"Tipo de tarjeta: Club Miles")
	def test_tema15_prueba_ID(self):
	#id:15
		msg=ofrecer_tarjeta_con_chip(3003, "C")
		self.assertEquals(msg,"Tipo de tarjeta: Advantage")
	def test_tema16_prueba_ID(self):
	#id:16
		msg=ofrecer_tarjeta_con_chip(3003, "F")
		self.assertEquals(msg,"Tipo de tarjeta: Clasica")
if __name__ == '__main__':
    unittest.main()