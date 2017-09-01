# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from Version_A import *
from Version_A import tema2
from Version_A.tema2 import clasificacion_clientes

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema2_1(self):
        msg = clasificacion_clientes(3000, False)
        self.assertEqual(msg, "Tipo de cliente: no es digno de crédito, Envio de boletin: No")

    def test_tema2_2(self):
        msg = clasificacion_clientes(30000, True)
        self.assertEqual(msg, "Tipo de cliente: AAA, Envio de boletin: Si")

    def test_tema2_3(self):
        msg = clasificacion_clientes(20001, True)
        self.assertEqual(msg, "Tipo de cliente: AA, Envio de boletin: Si")

    def test_tema2_4(self):
        msg = clasificacion_clientes(15001, True)
        self.assertEqual(msg, "Tipo de cliente: A, Envio de boletin: Si")

    def test_tema2_5(self):
        msg = clasificacion_clientes(10001, True)
        self.assertEqual(msg, "Tipo de cliente: B, Envio de boletin: Si")

    def test_tema2_6(self):
        msg = clasificacion_clientes(5001, True)
        self.assertEqual(msg, "Tipo de cliente: C, Envio de boletin: Si")

if __name__ == '__main__':
    unittest.main()