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
        
    def test_tema1_prueba_2(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(30)
        esperado = "escala: %s , eficiencia: %s" % ("A+", "los más eficientes")
        self.assertEquals(etiqueta, esperado)
        
    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(42)
        esperado = "escala: %s , eficiencia: %s" % ("A", "los más eficientes")
        self.assertEquals(etiqueta, esperado)
        
    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(55)
        esperado = "escala: %s , eficiencia: %s" % ("B", "los más eficientes")
        self.assertEquals(etiqueta, esperado)
        
    def test_tema1_prueba_5(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(75)
        esperado = "escala: %s , eficiencia: %s" % ("C", "los más eficientes")
        self.assertEquals(etiqueta, esperado)
        
    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(90)
        esperado = "escala: %s , eficiencia: %s" % ("D", "consumo medio")
        self.assertEquals(etiqueta, esperado)

if __name__ == '__main__':
    unittest.main()