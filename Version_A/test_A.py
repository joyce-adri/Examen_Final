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

    #tema 1 prueba 6 con un porcentaje de consumo de energía del 95%
    def test_tema1_prueba_6(self):
        etiqueta = tema1.etiquetado_consumo_energia(95);
        self.assertEqual(etiqueta, "escala: D , eficiencia: consumo medio");

    #tema 1 prueba 7 con un porcentaje de consumo de energía del 105%
    def test_tema1_prueba_7(self):
        etiqueta = tema1.etiquetado_consumo_energia(105);
        self.assertEqual(etiqueta, "escala: E , eficiencia: consumo medio");

    #tema 1 prueba 8 con un porcentaje de consumo de energía del 115%
    def test_tema1_prueba_8(self):
        etiqueta = tema1.etiquetado_consumo_energia(115);
        self.assertEqual(etiqueta, "escala: F , eficiencia: alto consumo energético");

    #tema 1 prueba 9 con un porcentaje de consumo de energía del 130%
    def test_tema1_prueba_9(self):
        etiqueta = tema1.etiquetado_consumo_energia(130);
        self.assertEqual(etiqueta, "escala: G , eficiencia: alto consumo energético");

    #tema 1 prueba 10 con un porcentaje de consumo de energía del -1%
    def test_tema1_prueba_10(self):
        etiqueta = tema1.etiquetado_consumo_energia(-1);
        self.assertEqual(etiqueta, "escala: ninguna , eficiencia: ninguno");


    #tema 2 prueba 1 con un monto de deposito de 50000
    def test_tema2_prueba_1(self):
        cc = tema2.clasificacion_clientes(50000, True)
        self.assertEqual(cc, "Tipo de cliente: AAA, Envio de boletin: Si")

    # tema 2 prueba 2 con un monto de deposito de 25000
    def test_tema2_prueba_2(self):
        cc = tema2.clasificacion_clientes(25000, True)
        self.assertEqual(cc, "Tipo de cliente: AA, Envio de boletin: Si")

    #tema 2 prueba 3 con un monto de deposito de 17000
    def test_tema2_prueba_3(self):
        cc = tema2.clasificacion_clientes(17000, True)
        self.assertEqual(cc, "Tipo de cliente: A, Envio de boletin: Si")

    #tema 2 prueba 4 con un monto de deposito de 12500
    def test_tema2_prueba_4(self):
        cc = tema2.clasificacion_clientes(12500, True)
        self.assertEqual(cc, "Tipo de cliente: B, Envio de boletin: Si")

    #tema 2 prueba 5 con un monto de deposito de 7000
    def test_tema2_prueba_5(self):
        cc = tema2.clasificacion_clientes(7000, True)
        self.assertEqual(cc, "Tipo de cliente: C, Envio de boletin: Si")

    # tema 2 prueba 6 con un monto de deposito de 2000
    def test_tema2_prueba_6(self) :
        cc = tema2.clasificacion_clientes(2000, False)
        self.assertEqual(cc, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

if __name__ == '__main__':
    unittest.main()