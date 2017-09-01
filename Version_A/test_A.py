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
        #Prueba 1
        self.assertEqual(tema1.etiquetado_consumo_energia(29),"escala: A++ , eficiencia: los más eficientes")
    def test_tema1_prueba_2(self):
        #Prueba 2
        self.assertEqual(tema1.etiquetado_consumo_energia(30),"escala: A+ , eficiencia: los más eficientes")
    def test_tema1_prueba_3(self):
        #Prueba 3
        self.assertEquals(tema1.etiquetado_consumo_energia(42),"escala: A , eficiencia: los más eficientes")
    def test_tema1_prueba_4(self):
        #Prueba 4
        self.assertEquals(tema1.etiquetado_consumo_energia(55),"escala: B , eficiencia: los más eficientes")
    def test_tema1_prueba_5(self):
        #Prueba 5
        self.assertEqual(tema1.etiquetado_consumo_energia(75),"escala: C , eficiencia: los más eficientes")
    def test_tema1_prueba_6(self):
        #Prueba 6
        self.assertEqual(tema1.etiquetado_consumo_energia(90),"escala: D , eficiencia: consumo medio")
    def test_tema1_prueba_7(self):
        #Prueba 7
        self.assertEqual(tema1.etiquetado_consumo_energia(100),"escala: E , eficiencia: consumo medio")
    def test_tema1_prueba_8(self):
        #Prueba 8
        self.assertEqual(tema1.etiquetado_consumo_energia(110),"escala: F , eficiencia: alto consumo energético")
    def test_tema1_prueba_9(self):
        #Prueba 9
        self.assertEqual(tema1.etiquetado_consumo_energia(500),"escala: G , eficiencia: alto consumo energético")
    def test_tema2_prueba_1(self):
        self.assertEqual(tema2.clasificacion_clientes(5000,True),"Tipo de cliente: C, Envio de boletin: Si","tema 2 correcto solo 1 caso")
        # inserte su codigo de prueba
        

if __name__ == '__main__':
    unittest.main()