# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import tema1
import tema2


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_tema1_prueba_1(self):
        porcentaje1=etiquetado_consumo_energia(25)
        self.assertEquals(porcentaje1,"escala: Lo más eficiente , eficiencia: A++ ")


    def test_tema1_prueba_2(self):
         porcentaje1 = etiquetado_consumo_energia(35)
         self.assertEquals(porcentaje1, "escala: Lo más eficiente , eficiencia: A+ ")


    def test_tema1_prueba_3(self):
        porcentaje1 = etiquetado_consumo_energia(50)
        self.assertEquals(porcentaje1, "escala: Lo más eficiente , eficiencia: A ")


    def test_tema1_prueba_4(self):
        porcentaje1 = etiquetado_consumo_energia(60)
        self.assertEquals(porcentaje1, "escala: Lo más eficiente , eficiencia: B ")


    def test_tema1_prueba_5(self):
        porcentaje1 = etiquetado_consumo_energia(80)
        self.assertEquals(porcentaje1, "escala: Lo más eficiente , eficiencia: C ")


    def test_tema1_prueba_6(self):
        porcentaje1 = etiquetado_consumo_energia(95)
        self.assertEquals(porcentaje1, "escala: consumo medio , eficiencia: D ")


    def test_tema1_prueba_7(self):
        porcentaje1 = etiquetado_consumo_energia(108)
        self.assertEquals(porcentaje1, "escala: consumo medio , eficiencia: E ")


    def test_tema1_prueba_8(self):
         porcentaje1 = etiquetado_consumo_energia(115)
         self.assertEquals(porcentaje1, "escala: alto consumo energético , eficiencia: F ")


    def test_tema1_prueba_9(self):
        porcentaje1 = etiquetado_consumo_energia(125)
        self.assertEquals(porcentaje1, "escala: alto conmsumo energético , eficiencia: G ")



    def test_tema2_prueba_1(self):
        clasificación=clasificacion_clientes(30200, "")
        self.assertEquals(clasificacion,"Tipo de cliente: AAA, Envio de boletin: Si")
    def test_tema2_prueba_2(self):
        clasificación=clasificacion_clientes(20800, "")
        self.assertEquals(clasificacion,"Tipo de cliente: AA, Envio de boletin: Si")
    def test_tema2_prueba_3(self):
        clasificación=clasificacion_clientes(15700, "")
        self.assertEquals(clasificacion,"Tipo de cliente: A, Envio de boletin: Si")
    def test_tema2_prueba_4(self):
        clasificación=clasificacion_clientes(12000, "")
        self.assertEquals(clasificacion,"Tipo de cliente: B, Envio de boletin: Si")
    def test_tema2_prueba_5(self):
        clasificación=clasificacion_clientes(6000, "")
        self.assertEquals(clasificacion,"Tipo de cliente: C, Envio de boletin: Si")
    def test_tema2_prueba_6(self):
        clasificación=clasificacion_clientes(300, "")
        self.assertEquals(clasificacion,"Tipo de cliente: no es digno de crédito, Envio de boletin: No")

if __name__ == '__main__':
    unittest.main()




