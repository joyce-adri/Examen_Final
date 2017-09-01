# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Version_A import *
import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
    def test_tema1_prueba_1(self):
        porcentaje = 85
        mensaje = etiquetado_consumo_energia(porcentaje)
        self.assertEquals(mensaje, "escala: C , eficiencia: los más eficientes")

    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()