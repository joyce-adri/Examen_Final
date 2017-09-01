# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_tema1_prueba_1A(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(0)
        print msg
        self.assertEquals(msg,"escala: A++ , eficiencia: los más eficientes")


    def test_tema1_prueba_2B(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(29)
        print msg
        self.assertEquals(msg, "escala: A++ , eficiencia: los más eficientes")


    def test_tema1_prueba_3C(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(30)
        print msg
        self.assertEquals(msg, "escala: A+ , eficiencia: los más eficientes")


    def test_tema1_prueba_4D(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(42)
        print msg
        self.assertEquals(msg, "escala: A , eficiencia: los más eficientes")


    def test_tema1_prueba_5E(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(55)
        print msg
        self.assertEquals(msg, "escala: B , eficiencia: los más eficientes")


    def test_tema1_prueba_6F(self):
            # inserte su codigo de prueba
            msg = tema1.etiquetado_consumo_energia(75)
            print msg
            self.assertEquals(msg,"escala: C , eficiencia: los más eficientes")


    def test_tema1_prueba_7G(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(90)
        print msg
        self.assertEquals(msg, "escala: D , eficiencia: consumo medio")

    def test_tema1_prueba_8H(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(91)
        print msg
        self.assertEquals(msg, "escala: D , eficiencia: consumo medio")

    def test_tema1_prueba_9I(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(100)
        print msg
        self.assertEquals(msg, "escala: E , eficiencia: consumo medio")

    def test_tema1_prueba_10J(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(110)
        print msg
        self.assertEquals(msg, "escala: F , eficiencia: alto consumo energético")

    def test_tema1_prueba_11K(self):
        # inserte su codigo de prueba
        msg = tema1.etiquetado_consumo_energia(126)
        print msg
        self.assertEquals(msg, "escala: G , eficiencia: alto consumo energético")








########################################################################################################################


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