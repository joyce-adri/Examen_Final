# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_1(self):
        res = "escala: A++ , eficiencia: los más eficientes"
        porcentaje = 15
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_2(self):
        res = "escala: A+ , eficiencia: los más eficientes"
        porcentaje = 40
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_3(self):
        res = "escala: A , eficiencia: los más eficientes"
        porcentaje = 50
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_4(self):
        res = "escala: B , eficiencia: los más eficientes"
        porcentaje = 70
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))


    def test_tema1_5(self):
        res = "escala: C , eficiencia: los más eficientes"
        porcentaje = 80
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_6(self):
        res = "escala: E , eficiencia: consumo medio"
        porcentaje = 100
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_7(self):
        res = "escala: D , eficiencia: consumo medio"
        porcentaje = 95
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_8(self):
        res = "escala: F , eficiencia: alto consumo energético"
        porcentaje = 120
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    def test_tema1_9(self):
        res = "escala: G , eficiencia: alto consumo energético"
        porcentaje = 130
        self.assertEquals(res, tema1.etiquetado_consumo_energia(porcentaje))

    # def test_tema2_prueba_ID(self):
        # inserte su codigo de prueba
        # self.assertEquals()

if __name__ == '__main__':
    unittest.main()