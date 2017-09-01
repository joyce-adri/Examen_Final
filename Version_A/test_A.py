# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    #tema 1 prueba 1 con un porcentaje de consumo de energía del 20%
    def test_tema1_prueba_1(self):
        etiqueta = tema1.etiquetado_consumo_energia(20);
        self.assertEqual(etiqueta, "escala: A++ , eficiencia: los más eficientes");

    #tema 1 prueba 2 con un porcentaje de consumo de energía del 35%
    def test_tema1_prueba_2(self):
        etiqueta = tema1.etiquetado_consumo_energia(35);
        self.assertEqual(etiqueta, "escala: A+ , eficiencia: los más eficientes");

    #tema 1 prueba 3 con un porcentaje de consumo de energía del 45%
    def test_tema1_prueba_3(self):
        etiqueta = tema1.etiquetado_consumo_energia(45);
        self.assertEqual(etiqueta, "escala: A , eficiencia: los más eficientes");

    #tema 1 prueba 4 con un porcentaje de consumo de energía del 60%
    def test_tema1_prueba_4(self):
        etiqueta = tema1.etiquetado_consumo_energia(60);
        self.assertEqual(etiqueta, "escala: B , eficiencia: los más eficientes");

    #tema 1 prueba 5 con un porcentaje de consumo de energía del 82%
    def test_tema1_prueba_5(self):
        etiqueta = tema1.etiquetado_consumo_energia(82);
        self.assertEqual(etiqueta, "escala: C , eficiencia: los más eficientes");



if __name__ == '__main__':
    unittest.main()