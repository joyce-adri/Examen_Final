# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

from tema1 import etiquetado_consumo_energia
class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
        eti = etiquetado_consumo_energia(20)
        self.assertEquals(eti, "escala: A++ , eficiencia: los más eficientes")
    def test_tema1_prueba_2(self):
        eti = etiquetado_consumo_energia(32)
        self.assertEquals(eti, "escala: A+ , eficiencia: los más eficientes")
    def test_tema1_prueba_3(self):
        eti = etiquetado_consumo_energia(45)
        self.assertEquals(eti, "escala: A , eficiencia: los más eficientes")
    def test_tema1_prueba_4(self):
        eti = etiquetado_consumo_energia(60)
        self.assertEquals(eti, "escala: B , eficiencia: los más eficientes")
    def test_tema1_prueba_5(self):
        eti = etiquetado_consumo_energia(80)
        self.assertEquals(eti, "escala: C , eficiencia: los más eficientes")

    def test_tema1_prueba_6(self):
        eti = etiquetado_consumo_energia(95)
        self.assertEquals(eti, "escala: D , eficiencia: consumo medio")
    def test_tema1_prueba_7(self):
        eti = etiquetado_consumo_energia(101)
        self.assertEquals(eti, "escala: E , eficiencia: consumo medio")

    def test_tema1_prueba_8(self):
        eti = etiquetado_consumo_energia(115)
        self.assertEquals(eti, "escala: F , eficiencia: alto consumo energético")
	#============================================#
"""
    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()
"""

if __name__ == '__main__':
    unittest.main()