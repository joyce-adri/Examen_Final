# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2



class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema2_1(self):
        msg = tema2.clasificacion_clientes(3000, False)
        self.assertEqual(msg, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

    def test_tema2_2(self):
        msg = tema2.clasificacion_clientes(30000, True)
        self.assertEqual(msg, "Tipo de cliente: AAA, Envio de boletin: Si")

    def test_tema2_3(self):
        msg = tema2.clasificacion_clientes(20001, True)
        self.assertEqual(msg, "Tipo de cliente: AA, Envio de boletin: Si")

    def test_tema2_4(self):
        msg = tema2.clasificacion_clientes(15001, True)
        self.assertEqual(msg, "Tipo de cliente: A, Envio de boletin: Si")

    def test_tema2_5(self):
        msg = tema2.clasificacion_clientes(10001, True)
        self.assertEqual(msg, "Tipo de cliente: B, Envio de boletin: Si")

    def test_tema2_6(self):
        msg = tema2.clasificacion_clientes(5001, True)
        self.assertEqual(msg, "Tipo de cliente: C, Envio de boletin: Si")

    def test_tema1_1(self):
        msg = tema1.etiquetado_consumo_energia(22)
        self.assertEqual(msg,"escala: A++ , eficiencia: los más eficientes")

    def test_tema1_2(self):
        msg = tema1.etiquetado_consumo_energia(32)
        self.assertEqual(msg,"escala: A+ , eficiencia: los más eficientes")

    def test_tema1_3(self):
        msg = tema1.etiquetado_consumo_energia(43)
        self.assertEqual(msg,"escala: A , eficiencia: los más eficientes")
    def test_tema1_4(self):
        msg = tema1.etiquetado_consumo_energia(61)
        self.assertEqual(msg,"escala: B , eficiencia: los más eficientes")

    def test_tema1_5(self):
        msg = tema1.etiquetado_consumo_energia(82)
        self.assertEqual(msg,"escala: C , eficiencia: los más eficientes")

    def test_tema1_6(self):
        msg = tema1.etiquetado_consumo_energia(91)
        self.assertEqual(msg,"escala: D , eficiencia: consumo medio")

if __name__ == '__main__':
    unittest.main()