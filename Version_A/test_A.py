# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
	
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
	
	def test_tema1_prueba_1(self):
		result = tema1.etiquetado_consumo_energia(20)
		self.assertEquals(result, "escala: A++ , eficiencia: los más eficientes", "failure")

	def test_tema1_prueba_2(self):
		result = tema1.etiquetado_consumo_energia(40)
		self.assertEquals(result, "escala: A+ , eficiencia: los más eficientes", "failure")

	def test_tema1_prueba_3(self):
		result = tema1.etiquetado_consumo_energia(50)
		self.assertEquals(result, "escala: A , eficiencia: los más eficientes", "failure")

	def test_tema1_prueba_4(self):
		result = tema1.etiquetado_consumo_energia(60)
		self.assertEquals(result, "escala: B , eficiencia: los más eficientes", "failure")

	def test_tema1_prueba_5(self):
		result = tema1.etiquetado_consumo_energia(80)
		self.assertEquals(result, "escala: C , eficiencia: los más eficientes", "failure")

	def test_tema1_prueba_6(self):
		result = tema1.etiquetado_consumo_energia(95)
		self.assertEquals(result, "escala: D , eficiencia: consumo medio", "failure")

	def test_tema1_prueba_7(self):
		result = tema1.etiquetado_consumo_energia(105)
		self.assertEquals(result, "escala: E , eficiencia: consumo medio", "failure")

	def test_tema1_prueba_8(self):
		result = tema1.etiquetado_consumo_energia(110)
		self.assertEquals(result, "escala: F , eficiencia: alto consumo energético", "failure")

	def test_tema1_prueba_9(self):
		result = tema1.etiquetado_consumo_energia(130)
		self.assertEquals(result, "escala: G , eficiencia: alto consumo energético", "failure")

	def test_tema2_prueba_1(self):
		result = tema2.clasificacion_clientes(0, False)
		self.assertEquals(result, "Tipo de cliente: no es digno de crédito, Envio de boletin: No", "failure")

	def test_tema2_prueba_2(self):
		result = tema2.clasificacion_clientes(35000, True)
		self.assertEquals(result, "Tipo de cliente: AAA, Envio de boletin: Si", "failure")

	def test_tema2_prueba_3(self):
		result = tema2.clasificacion_clientes(25000, True)
		self.assertEquals(result, "Tipo de cliente: AA, Envio de boletin: Si", "failure")

	def test_tema2_prueba_4(self):
		result = tema2.clasificacion_clientes(17000, True)
		self.assertEquals(result, "Tipo de cliente: A, Envio de boletin: Si", "failure")

	def test_tema2_prueba_5(self):
		result = tema2.clasificacion_clientes(12000, True)
		self.assertEquals(result, "Tipo de cliente: B, Envio de boletin: Si", "failure")

if __name__ == '__main__':
	unittest.main()