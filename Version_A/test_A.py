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
        
    def test_tema1_prueba_7(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(100)
        esperado = "escala: %s , eficiencia: %s" % ("E", "consumo medio")
        self.assertEquals(etiqueta, esperado)

    def test_tema1_prueba_8(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(110)
        esperado = "escala: %s , eficiencia: %s" % ("F", "alto consumo energético")
        self.assertEquals(etiqueta, esperado)
        
    def test_tema1_prueba_9(self):
        # inserte su codigo de prueba
        etiqueta = tema1.etiquetado_consumo_energia(126)
        esperado = "escala: %s , eficiencia: %s" % ("G", "alto consumo energético")
        self.assertEquals(etiqueta, esperado)
        
    def test_tema2_prueba_1(self):
        # inserte su codigo de prueba
        clasificacion = tema2.clasificacion_clientes(0, False)
        esperado = "Tipo de cliente: %s, Envio de boletin: %s" % ("no es digno de crédito", "No")
        self.assertEquals(clasificacion, esperado)
        
    def test_tema2_prueba_2(self):
        # inserte su codigo de prueba
        clasificacion = tema2.clasificacion_clientes(30000, True)
        esperado = "Tipo de cliente: %s, Envio de boletin: %s" % ("AAA", "Si")
        self.assertEquals(clasificacion, esperado)
        
    def test_tema2_prueba_3(self):
        # inserte su codigo de prueba
        clasificacion = tema2.clasificacion_clientes(20000, True)
        esperado = "Tipo de cliente: %s, Envio de boletin: %s" % ("AA", "Si")
        self.assertEquals(clasificacion, esperado)
        
    def test_tema2_prueba_4(self):
        # inserte su codigo de prueba
        clasificacion = tema2.clasificacion_clientes(15000, True)
        esperado = "Tipo de cliente: %s, Envio de boletin: %s" % ("A", "Si")
        self.assertEquals(clasificacion, esperado)
    
if __name__ == '__main__':
    unittest.main()