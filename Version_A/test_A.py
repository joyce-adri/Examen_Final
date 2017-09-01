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
        etiqueta = tema1.etiquetado_consumo_energia(0)
        esperado = "escala: %s , eficiencia: %s" % ("A++", "los más eficientes")
        self.assertEquals(etiqueta, esperado)

    def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        self.assertEquals()

if __name__ == '__main__':
    unittest.main()