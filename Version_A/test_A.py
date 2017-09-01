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
        print("Prueba 1")
        msg = tema1.etiquetado_consumo_energia(-1)
        self.assertEquals(msg, "escala: ninguna , eficiencia: ninguno")

    def test_tema1_prueba_2(self):
        # inserte su codigo de prueba
        print("Prueba 2")
        msg = tema1.etiquetado_consumo_energia(25)
        self.assertEquals(msg, "escala: A++ , eficiencia: los más eficientes")

    def test_tema1_prueba_3(self):
        # inserte su codigo de prueba
        print("Prueba 3")
        msg = tema1.etiquetado_consumo_energia(35)
        self.assertEquals(msg, "escala: A+ , eficiencia: los más eficientes")

    def test_tema1_prueba_4(self):
        # inserte su codigo de prueba
        print("Prueba 4")
        msg = tema1.etiquetado_consumo_energia(45)
        self.assertEquals(msg, "escala: A , eficiencia: los más eficientes")

    def test_tema1_prueba_5(self):
        # inserte su codigo de prueba
        print("Prueba 5")
        msg = tema1.etiquetado_consumo_energia(55)
        self.assertEquals(msg, "escala: B , eficiencia: los más eficientes")

    def test_tema1_prueba_6(self):
        # inserte su codigo de prueba
        print("Prueba 6")
        msg = tema1.etiquetado_consumo_energia(75)
        self.assertEquals(msg, "escala: C , eficiencia: los más eficientes")

    def test_tema1_prueba_7(self):
        # inserte su codigo de prueba
        print("Prueba 7")
        msg = tema1.etiquetado_consumo_energia(95)
        self.assertEquals(msg, "escala: D , eficiencia: consumo medio")

    def test_tema1_prueba_8(self):
        # inserte su codigo de prueba
        print("Prueba 8")
        msg = tema1.etiquetado_consumo_energia(105)
        self.assertEquals(msg, "escala: E , eficiencia: consumo medio")

    def test_tema1_prueba_9(self):
        # inserte su codigo de prueba
        print("Prueba 9")
        msg = tema1.etiquetado_consumo_energia(115)
        self.assertEquals(msg, "escala: F , eficiencia: alto consumo energético")

    def test_tema1_prueba_10(self):
        # inserte su codigo de prueba
        print("Prueba 10")
        msg = tema1.etiquetado_consumo_energia(135)
        self.assertEquals(msg, "escala: G , eficiencia: alto consumo energético")

    #def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
    #    self.assertEquals()

if __name__ == '__main__':
    unittest.main()