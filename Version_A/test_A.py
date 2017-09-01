# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
        etiqueta = tema1.etiquetado_consumo_energia(20);
        self.assertEqual(etiqueta, "escala: A++ , eficiencia: los más eficientes");

    def test_tema1_prueba_2(self):
        etiqueta = tema1.etiquetado_consumo_energia(35);
        self.assertEqual(etiqueta, "escala: A+ , eficiencia: los más eficientes");

    def test_tema1_prueba_3(self):
        etiqueta = tema1.etiquetado_consumo_energia(45);
        self.assertEqual(etiqueta, "escala: A , eficiencia: los más eficientes");

    def test_tema1_prueba_4(self):
        etiqueta = tema1.etiquetado_consumo_energia(60);
        self.assertEqual(etiqueta, "escala: B , eficiencia: los más eficientes");

    def test_tema1_prueba_5(self):
        etiqueta = tema1.etiquetado_consumo_energia(82);
        self.assertEqual(etiqueta, "escala: C , eficiencia: los más eficientes");

    def test_tema1_prueba_6(self):
        etiqueta = tema1.etiquetado_consumo_energia(95);
        self.assertEqual(etiqueta, "escala: D , eficiencia: consumo medio");

    def test_tema1_prueba_7(self):
        etiqueta = tema1.etiquetado_consumo_energia(105);
        self.assertEqual(etiqueta, "escala: E , eficiencia: consumo medio");

    def test_tema1_prueba_8(self):
        etiqueta = tema1.etiquetado_consumo_energia(115);
        self.assertEqual(etiqueta, "escala: F , eficiencia: alto consumo energético");

    def test_tema1_prueba_9(self):
        etiqueta = tema1.etiquetado_consumo_energia(130);
        self.assertEqual(etiqueta, "escala: G , eficiencia: alto consumo energético");

    def test_tema1_prueba_10(self):
        etiqueta = tema1.etiquetado_consumo_energia(-1);
        self.assertEqual(etiqueta, "escala: ninguna , eficiencia: ninguno");


#----------------------------------------------------------------------------------------

    def test_tema2_prueba_1(self):
        cc = tema2.clasificacion_clientes(50000, True)
        self.assertEqual(cc, "Tipo de cliente: AAA, Envio de boletin: Si")

    def test_tema2_prueba_2(self):
        cc = tema2.clasificacion_clientes(25000, True)
        self.assertEqual(cc, "Tipo de cliente: AA, Envio de boletin: Si")

    def test_tema2_prueba_3(self):
        cc = tema2.clasificacion_clientes(17000, True)
        self.assertEqual(cc, "Tipo de cliente: A, Envio de boletin: Si")

    def test_tema2_prueba_4(self):
        cc = tema2.clasificacion_clientes(12500, True)
        self.assertEqual(cc, "Tipo de cliente: B, Envio de boletin: Si")

    def test_tema2_prueba_5(self):
        cc = tema2.clasificacion_clientes(7000, True)
        self.assertEqual(cc, "Tipo de cliente: C, Envio de boletin: Si")

    def test_tema2_prueba_6(self) :
        cc = tema2.clasificacion_clientes(2000, False)
        self.assertEqual(cc, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

if __name__ == '__main__':
    unittest.main()