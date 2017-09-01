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
        # inserte su codigo de prueba
        eti = etiquetado_consumo_energia(20)
        self.assertEquals(eti, "escala: A++ , eficiencia: los más eficientes")

	#============================================#
"""
    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()
"""

if __name__ == '__main__':
    unittest.main()