# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    #def test_tema1_prueba_ID(self):
        # inserte su codigo de prueba
    #    self.assertEquals()

    def test_tema2_prueba_1A(self):
        # inserte su codigo de prueba
        msg = tema2.clasificacion_clientes(30000, True)
        print msg
        self.assertAlmostEquals(msg,"Tipo de cliente: AAA, Envio de boletin: Si")

    def test_tema2_prueba_2B(self):
        # inserte su codigo de prueba
        msg = tema2.clasificacion_clientes(20000, True)
        print msg
        self.assertAlmostEquals(msg,"Tipo de cliente: AA, Envio de boletin: Si")

    def test_tema2_prueba_3C(self):
        # inserte su codigo de prueba
        msg = tema2.clasificacion_clientes(15000, True)
        print msg
        self.assertAlmostEquals(msg,"Tipo de cliente: A, Envio de boletin: Si")

    def test_tema2_prueba_4D(self):
        # inserte su codigo de prueba
        msg = tema2.clasificacion_clientes(10000, True)
        print msg
        self.assertAlmostEquals(msg,"Tipo de cliente: B, Envio de boletin: Si")

    def test_tema2_prueba_5E(self):
        # inserte su codigo de prueba
        msg = tema2.clasificacion_clientes(5000, True)
        print msg
        self.assertAlmostEquals(msg,"Tipo de cliente: C, Envio de boletin: Si")

    def test_tema2_prueba_6F(self):
        # inserte su codigo de prueba
        msg = tema2.clasificacion_clientes(30000, False)
        print msg
        self.assertAlmostEquals(msg,"Tipo de cliente: no es digno de crédito, Envio de boletin: No")

if __name__ == '__main__':
    unittest.main()